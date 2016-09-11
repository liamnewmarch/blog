export function registerServiceWorker() {
  if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/js/service-worker.js', {
      scope: '/'
    });
  }
}
