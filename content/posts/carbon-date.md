---
date: 2013-05-08
summary: (Obsolete) A tool for estimating the age of a webpage by its jQuery version.
layout: posts/post.njk
tags: post
title: Carbon Date for jQuery
unlisted: true
---

__2020 edit: This project has been discontinued. It was a fun idea, but never really useful.__

Occasionally when I’m browsing the web I want to know how old a website is.

Maybe it does something awesome and innovative. Maybe it's terrible and due a redesign. Whatever the reason, it'd be useful to know how old the site is. The trouble is unless the author explicitly puts a date on the site, there often isn't a good way to age it.

Unless they use jQuery.

See, web developers generally grab the latest jQuery version and don’t update it. By looking at the version number (specifically in `jQuery.fn.jquery`) we can approximate the date of the last build / redesign.

[Carbon date](https://github.com/liamnewmarch/carbon-date) is a tiny tool that does just that.


## Get the bookmarklet

Carbon date is a bookmarklet – to use it drag the following link to your bookmark toolbar:

~~Carbon date~~ (Sorry!)

If you'd like to see the (tiny) unminified source or would like to report have a bug, you can find the project [on GitHub.](https://github.com/liamnewmarch/carbon-date)

Happy dating!
