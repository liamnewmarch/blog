/** @type {NodeListOf<HTMLLinkElement>} */
const preloadLinks = document.querySelectorAll('link[rel="preload"]');

// Activate preload link elements
for (const element of preloadLinks) {
  element.rel = 'stylesheet';
}
