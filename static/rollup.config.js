import browsersync from 'rollup-plugin-browsersync';
import css from 'rollup-plugin-css-only';
import copy from 'rollup-plugin-copy';
import { terser } from 'rollup-plugin-terser';

const isWatch = Boolean(process.env.ROLLUP_WATCH);
const isProduction = process.env.NODE_ENV === 'production';

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
    copy({
      copyOnce: true,
      flatten: false,
      targets: [{
        src: [
          'src/*.png',
          'src/*.txt',
        ],
        dest: 'build',
      }],
    }),
    isProduction && terser(),
  ],
};
