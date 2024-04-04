---
date: 2018-07-25
title: 'CSS tip: flipping elements'
summary: Mirror the real world by flipping your icons with CSS, rather than rotating.
image:
  url: /posts/img/css-tip-flipping-elements.avif
  width: 1554
  height: 1166
---

Sometimes, when building out a website you might come across the same icon in different orientations. A common example of this is when you have an arrow pointing left and an arrow pointing right which are otherwise identical. In situations like this you can use [CSS transforms](https://developer.mozilla.org/en-US/docs/Web/CSS/transform) instead of serving two images.

A common pattern I see is to use `transform: rotate` in CSS.

```css
.next,
.previous {
  background-image: url('/images/arrow.png');
}

.previous {
  transform: rotate(180deg);
}
```

This works for images which are vertically symmetrical but for anything else the transformed icon will be upside down. For that reason, it’s a better practice to use `transform: scaleX` or `transform: scaleY` instead – that way your images will be natural mirror images:

```css
.previous {
  transform: scaleX(-1);
}
```

[Check out this example](https://codepen.io/liamnewmarch/embed/xJrpxW) to see it in action.
