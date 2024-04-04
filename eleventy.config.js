import syntaxHighlight from '@11ty/eleventy-plugin-syntaxhighlight'
import { minify } from 'html-minifier'
import yaml from 'js-yaml'

export default function(config) {
  // Copy static files
  config.addPassthroughCopy({ static: '/' })

  // Code block syntax highlighting
  config.addPlugin(syntaxHighlight)

  // Minify all HTML output
  config.addTransform('htmlmin', (content, path) => {
    if (!path.endsWith('.html')) return content
    return minify(content, {
      collapseBooleanAttributes: true,
      collapseWhitespace: true,
      decodeEntities: true,
      keepClosingSlash: false,
      removeComments: true,
      sortAttributes: true,
      sortClassName: true,
    })
  })

  // Template filter to format dates
  config.addFilter('date', (date, format = 'iso') => {
    switch (format) {
      case 'long':
        return new Intl.DateTimeFormat('en', {
          day: 'numeric',
          month: 'long',
          year: 'numeric',
        }).format(date)
      case 'iso':
      default:
        return date.toISOString().split('T')[0]
    }
  })

  // Template filter to limit an array length
  config.addFilter('limit', (items, limit, offset = 0) => {
    return items.slice(offset, limit)
  })

  // Template filter to filter unlisted posts
  config.addFilter('published', (posts) => {
    return posts.filter((post) => !post.data.unlisted)
  })

  // Support YAML global data files
  config.addDataExtension('yaml', (contents) => {
    return yaml.load(contents)
  })

  // Change default dirs
  return {
    dir: {
      data: '../data',
      includes: '../templates',
      input: 'content',
      output: 'build',
    },
    markdownTemplateEngine: 'njk',
  }
}
