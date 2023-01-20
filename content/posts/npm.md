---
date: 2014-08-18
summary: A short guide to updating globally installed npm packages.
layout: posts/post.njk
tags: post
title: Updating npm packages
unlisted: true
---

In a previous version of this post I explained how npm doesn’t work like other package management systems you might be familiar with. My advice was to avoid running `npm -g update`. Hopefully good advice at the time, but thankfully no longer necessary.

The problem was, with version < 2.6.1, npm would upgrade itself to a cutting edge version which would often be broken. The work around was to detect outdated packages and install them manually. npm 2.6.1 and above correct this issue and will only update itself to the latest *stable* version.

The process for detecting outdated packages hasn’t changed, and can be useful if you don’t want to update everything at once:

```shell
npm -g outdated --depth=0
```

From there you can update a single package by reinstalling it:

```shell
npm -g install package-name
```
