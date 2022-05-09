import StackdriverErrorReporter from 'stackdriver-errors-js';

/** @type {StackdriverErrorReporter} */
const reporter = new StackdriverErrorReporter();

reporter.start({
  disabled: 'debug' in document.body.dataset,
  key: document.body.dataset.stackdriverApiKey,
  projectId: document.body.dataset.googleCloudProject,
});
