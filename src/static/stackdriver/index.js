import StackdriverErrorReporter from 'stackdriver-errors-js';

/**
 * @param {HTMLElement} element
 * @param {string} key
 * @returns {boolean}
 */
function booleanDataAttribute({ dataset }, key) {
  return key in dataset && dataset[key].toLowerCase() !== 'false';
}

/** @type {StackdriverErrorReporter} */
const reporter = new StackdriverErrorReporter();

reporter.start({
  disabled: booleanDataAttribute(document.body, 'debug'),
  key: document.body.dataset.stackdriverApiKey,
  projectId: document.body.dataset.googleCloudProject,
});
