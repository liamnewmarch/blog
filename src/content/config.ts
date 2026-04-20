import { defineCollection, z } from 'astro:content'
import { glob } from 'astro/loaders'

const pages = defineCollection({
  loader: glob({
    base: './content',
    pattern: '*.md',
  }),
  schema: z.object({
    title: z.string().optional(),
    links: z.array(z.object({
      name: z.string(),
      url: z.string(),
      username: z.string().optional(),
    })).optional(),
    pages: z.array(z.object({
      title: z.string(),
      url: z.string(),
    })).optional(),
  }),
})

const posts = defineCollection({
  loader: glob({
    base: './content/posts',
    pattern: '**/*.md',
  }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    summary: z.string(),
    unlisted: z.boolean().optional(),
    image: z.object({
      url: z.string(),
      alt: z.string().optional(),
      width: z.number().optional(),
      height: z.number().optional(),
    }).optional(),
  }),
})

export const collections = { pages, posts }
