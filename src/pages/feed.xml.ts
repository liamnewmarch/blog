import rss from '@astrojs/rss'
import { getCollection } from 'astro:content'
import type { APIContext } from 'astro'

export async function GET(context: APIContext) {
  const allPosts = await getCollection('posts')
  const items = allPosts
      .filter((post) => !post.data.unlisted)
      .sort((a, b) => b.data.date.getTime() - a.data.date.getTime())
      .slice(0, 10)
      .map((post) => ({
        title: post.data.title,
        pubDate: post.data.date,
        description: post.data.summary,
        link: `/posts/${post.id}/`,
      }))

  return rss({
    title: 'Liam Newmarch',
    description: 'Liam Newmarch lives in Yorkshire and makes things for the web.',
    site: context.site!,
    items,
    customData: '<language>en-GB</language>',
  })
}
