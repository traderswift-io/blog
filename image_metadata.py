import struct
import xml.etree.ElementTree as element_tree
import zlib
from pathlib import Path


def png_dimensions(data):
    if not data.startswith(b'\x89PNG\r\n\x1a\n'):
        raise ValueError('invalid PNG signature')
    position = 8
    dimensions = None
    compressed_pixels = bytearray()
    while position < len(data):
        if position + 12 > len(data):
            raise ValueError('truncated PNG chunk')
        length = int.from_bytes(data[position:position + 4], 'big')
        chunk_type = data[position + 4:position + 8]
        end = position + 8 + length
        if end + 4 > len(data):
            raise ValueError('truncated PNG data')
        payload = data[position + 8:end]
        if zlib.crc32(data[position + 4:end]) != int.from_bytes(data[end:end + 4], 'big'):
            raise ValueError('PNG checksum mismatch')
        if dimensions is None and chunk_type != b'IHDR':
            raise ValueError('PNG must begin with IHDR')
        if chunk_type == b'IHDR':
            if dimensions or length != 13:
                raise ValueError('invalid PNG IHDR')
            width, height, depth, color, compression, filtering, interlace = struct.unpack('>IIBBBBB', payload)
            allowed_depths = {0: (1, 2, 4, 8, 16), 2: (8, 16), 3: (1, 2, 4, 8), 4: (8, 16), 6: (8, 16)}
            if not width or not height or depth not in allowed_depths.get(color, ()) or compression or filtering or interlace > 1:
                raise ValueError('invalid PNG image header')
            dimensions = width, height
        elif chunk_type == b'IDAT':
            compressed_pixels.extend(payload)
        elif chunk_type == b'IEND':
            if length or end + 4 != len(data) or not compressed_pixels:
                raise ValueError('invalid PNG ending')
            decoder = zlib.decompressobj()
            pixels = decoder.decompress(compressed_pixels)
            if not decoder.eof or decoder.unused_data or not pixels:
                raise ValueError('invalid PNG compressed pixels')
            if not interlace:
                channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[color]
                row_bytes = (width * depth * channels + 7) // 8 + 1
                if len(pixels) != row_bytes * height or any(pixels[offset] > 4 for offset in range(0, len(pixels), row_bytes)):
                    raise ValueError('invalid PNG scanlines')
            return dimensions
        position = end + 4
    raise ValueError('missing PNG ending')


def jpeg_dimensions(data):
    if not data.startswith(b'\xff\xd8'):
        raise ValueError('invalid JPEG signature')
    position = 2
    dimensions = None
    scan_seen = False
    tables = set()
    while position < len(data):
        if data[position] != 255:
            raise ValueError('invalid JPEG marker')
        while position < len(data) and data[position] == 255:
            position += 1
        if position == len(data):
            break
        marker = data[position]
        position += 1
        if marker == 217:
            if not dimensions or not scan_seen or not {196, 219} <= tables or position != len(data):
                raise ValueError('incomplete JPEG image')
            return dimensions
        if marker in (0, 216) or 208 <= marker <= 215:
            raise ValueError('unexpected JPEG marker')
        if position + 2 > len(data):
            break
        length = int.from_bytes(data[position:position + 2], 'big')
        if length < 2 or position + length > len(data):
            raise ValueError('truncated JPEG segment')
        payload = data[position + 2:position + length]
        position += length
        if marker in (192, 193, 194):
            if dimensions or len(payload) < 9 or len(payload) != 6 + 3 * payload[5]:
                raise ValueError('invalid JPEG frame')
            height, width = struct.unpack('>HH', payload[1:5])
            if not width or not height or payload[0] not in (8, 12):
                raise ValueError('invalid JPEG dimensions')
            dimensions = width, height
        elif marker in (196, 219):
            if not payload:
                raise ValueError('empty JPEG table')
            tables.add(marker)
        elif marker == 218:
            if not dimensions or not payload or len(payload) != 4 + 2 * payload[0]:
                raise ValueError('invalid JPEG scan header')
            scan_seen = True
            scan_start = position
            while position < len(data):
                if data[position] != 255:
                    position += 1
                elif position + 1 < len(data) and (data[position + 1] == 0 or 208 <= data[position + 1] <= 215):
                    position += 2
                else:
                    break
            if position == scan_start:
                raise ValueError('empty JPEG scan')
    raise ValueError('missing JPEG ending')


def image_dimensions(image_path):
    image_path = Path(image_path)
    try:
        if image_path.suffix.lower() == '.svg':
            root = element_tree.parse(image_path).getroot()
            width, height = root.get('width', ''), root.get('height', '')
            if not width.isdigit() or not height.isdigit() or int(width) < 1 or int(height) < 1:
                raise ValueError('SVG needs positive numeric width and height')
            return int(width), int(height)
        if image_path.suffix.lower() == '.png':
            return png_dimensions(image_path.read_bytes())
        if image_path.suffix.lower() in ('.jpg', '.jpeg'):
            return jpeg_dimensions(image_path.read_bytes())
        raise ValueError('supported formats are SVG, PNG and JPEG')
    except (OSError, ValueError, element_tree.ParseError, struct.error, zlib.error) as error:
        raise ValueError(f'Invalid image {image_path.name}: {error}') from error
