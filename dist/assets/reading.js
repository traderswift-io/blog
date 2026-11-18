(() => {
const root = document.documentElement;
if (root.dataset.skin === 'control') {
const preference = matchMedia('(prefers-color-scheme: dark)');
const readTheme = () => {
try {
const saved = localStorage.getItem('theme');
if (saved === 'light' || saved === 'dark') root.dataset.theme = saved;
else delete root.dataset.theme;
} catch {}
};
readTheme();
const targetTheme = () => (root.dataset.theme || (preference.matches ? 'dark' : 'light')) === 'dark' ? 'light' : 'dark';
const updateThemeButton = () => document.querySelector('.theme-switch')?.setAttribute('aria-label', `Switch to ${targetTheme()} mode`);
for (const type of ['pageshow', 'pagereveal']) addEventListener(type, event => {
if (event.type === 'pageshow' && !event.persisted) return;
readTheme();
updateThemeButton();
});
addEventListener('DOMContentLoaded', () => {
const button = document.querySelector('.theme-switch');
updateThemeButton();
button.hidden = false;
button.addEventListener('click', () => {
root.dataset.theme = targetTheme();
try { localStorage.setItem('theme', root.dataset.theme); } catch {}
updateThemeButton();
});
});
preference.addEventListener('change', updateThemeButton);
}
history.scrollRestoration = 'manual';
const resetScroll = () => {
if (!location.hash) scrollTo(0, 0);
const chip = document.querySelector('.chapter-progress [aria-current]');
if (chip) {
const row = chip.parentElement;
row.scrollLeft += chip.getBoundingClientRect().left - row.getBoundingClientRect().left - (row.clientWidth - chip.offsetWidth) / 2;
}
};
for (const event of ['DOMContentLoaded', 'pageshow']) addEventListener(event, resetScroll);
const link = relation => document.querySelector(`a[rel="${relation}"]`);
const direction = (transition, backwards) => {
for (const promise of ['ready', 'finished', 'updateCallbackDone']) transition?.[promise]?.catch(() => {});
transition?.types?.add(backwards ? 'back' : 'forward');
};
addEventListener('pageswap', event => {
direction(event.viewTransition, event.activation?.entry?.url === link('prev')?.href);
});
addEventListener('pagereveal', event => {
resetScroll();
direction(event.viewTransition, globalThis.navigation?.activation?.from?.url === link('next')?.href);
});
let start;
addEventListener('touchstart', event => {
start = undefined;
if (event.touches.length !== 1 || event.target.closest('a, button, input, textarea, select, pre, .table-scroll, .prompt, [contenteditable]')) return;
const touch = event.touches[0];
if (touch.clientX < 24 || touch.clientX > innerWidth - 24) return;
start = { x: touch.clientX, y: touch.clientY };
}, { passive: true });
addEventListener('touchmove', event => {
if (event.touches.length !== 1 || (start && Math.abs(event.touches[0].clientY - start.y) > 40)) start = undefined;
if (start && event.cancelable && Math.abs(event.touches[0].clientX - start.x) > Math.abs(event.touches[0].clientY - start.y)) event.preventDefault();
}, { passive: false });
addEventListener('touchcancel', () => { start = undefined; });
addEventListener('touchend', event => {
const origin = start;
start = undefined;
if (!origin || event.touches.length || !getSelection()?.isCollapsed) return;
const touch = event.changedTouches[0];
const distance = touch.clientX - origin.x;
if (Math.abs(distance) < Math.max(70, innerWidth * .2) || Math.abs(touch.clientY - origin.y) > 40) return;
const target = link(distance < 0 ? 'next' : 'prev');
if (target) location.assign(target.href);
}, { passive: true });
})();
