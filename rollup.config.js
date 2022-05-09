import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import browsersync from 'rollup-plugin-browsersync';
import css from 'rollup-plugin-css-only';
import copy from 'rollup-plugin-copy';
import { terser } from 'rollup-plugin-terser';

const isWatch = Boolean(process.env.ROLLUP_WATCH);
const isProduction = process.env.NODE_ENV === 'production';

export default {
  input: 'src/static/index.js',
  output: {
    file: 'src/static/bundle.js',
    format: 'es',
  },
  plugins: [
    resolve(),
    commonjs(),
    isWatch && browsersync({
      open: false,
      proxy: 'django:8000',
    }),
    css({
      output: 'bundle.css',
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
  watch: {
    clearScreen: false,
  },
};
