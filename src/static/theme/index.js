import { ThemeController } from './controller.js';

/** @type {NodeListOf<HTMLLinkElement>} */
const preloadLinks = document.querySelectorAll('link[rel="preload"]');

/** @type {ThemeController} */
const theme = new ThemeController();

/** @type {NodeListOf<HTMLElement>} */
const toggles = document.querySelectorAll('.toggle-theme');

// Activate preload link elements
for (const element of preloadLinks) {
  element.rel = 'stylesheet';
}

// Toggle the theme when a button is clicked
for (const element of toggles) {
  element.hidden = false;
  element.addEventListener('click', (event) => {
    event.preventDefault();
    theme.toggle();
  });
}

// Update icons when the theme changes
document.addEventListener('toggle-theme', ({ detail }) => {
  document.documentElement.dataset.theme = detail.name;
  for (const element of toggles) {
    element.dataset.icon = detail.icon;
  }
});

theme.reset();
