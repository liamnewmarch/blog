import type { AstroUserConfig } from 'astro'

export default {
  site: 'https://liam.nwmr.ch',
  outDir: 'build',
  compressHTML: true,
  markdown: {
    syntaxHighlight: 'prism',
  },
} satisfies AstroUserConfig
