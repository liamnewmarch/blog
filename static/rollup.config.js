import browsersync from 'rollup-plugin-browsersync';
import css from 'rollup-plugin-css-only';

const isWatch = Boolean(process.env.ROLLUP_WATCH);

export default {
  input: 'src/index.js',
  output: {
    dir: 'build',
    format: 'es',
  },
  plugins: [
    isWatch && browsersync({
      open: false,
      proxy: 'django:8000',
    }),
    css({
      output: 'index.css',
    }),
  ],
};
