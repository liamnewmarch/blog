import type { AstroUserConfig } from 'astro'

const rollupOptions = {
  output: {
    assetFileNames: 'static/[hash][extname]',
    chunkFileNames: 'static/[hash].js',
    entryFileNames: 'static/[hash].js',
  },
}

export default {
  site: 'https://liam.nwmr.ch',
  outDir: 'build',
  build: {
    assets: 'static',
    inlineStylesheets: 'never',
  },
  compressHTML: true,
  markdown: {
    syntaxHighlight: 'prism',
  },
  vite: {
    build: {
      assetsInlineLimit: 0, // prevent JS from being inlined
      rollupOptions, // TODO remove when CSS uses environments...
    },
    environments: {
      client: {
        build: {
          rollupOptions,
        },
      },
    },
  },
} satisfies AstroUserConfig
