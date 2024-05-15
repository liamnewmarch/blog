---
date: 2024-05-16
title: Responsive design and accessibility in 2024
summary: How to level up your responsive web design for Accessibility Awareness Day
image:
  url: /posts/img/responsive-design-and-accessibility-in-2024.avif
  width: 1920
  height: 1280
---

_Cover photo by [Kelly Sikkema](https://unsplash.com/@kellysikkema) on [Unsplash](https://unsplash.com/photos/a-person-writing-on-a-piece-of-paper-next-to-a-keyboard-Cg60_WXjvC4)._

This Accessibility Awareness Day I want to take a look at a recent addition to CSS which makes it easier than ever to build adaptable and inclusive interfaces. If your goal is to put your idea in front of as many people as possible by supporting a wide variety of devices, then read on.

## A decade of best practices

One of the most common ways web developers practise inclusivity is through responsive web design – the technique of making web pages resize and adjust their layout to fit the user’s device.

You might not think that making your front-end responsive is an accessibility consideration because of how ubiquitous it is, but make no mistake. Accessibility is all about making an experience that is usable by everyone, and that starts with supporting a variety of devices, form factors, window sizes and zoom levels.

For many projects over the last decade, responsive web design has changed from being a nice-to-have consideration, to an expected requirement.


![A Google Trends graph showing search interest in “Responsive web design”. Interest starts in early 2011 and peaks around 2014 with a long tail until the present day.](/posts/img/responsive-design-trend.avif)

_Source [Google Trends](https://trends.google.co.uk/trends/explore?date=2010-01-01+2024-05-15&q=Responsive+web+design)._

## The status quo

Making a page responsive starts with adding a _meta tag_ to your HTML. This tells the browser not to treat it like a zoomed-out desktop page on mobile.

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- Tell the browser this web page is responsive -->
    <meta name="viewport" content="initial-scale=1, width=device-width">
```

As you style your page with CSS, you can use _media queries_ to change the page layout depending on the width of the browser’s viewport.

```css
/* General styles */
article {
  font-family: Helvetica, Arial, sans-serif;

  /* Show two columns if the browser is more than 640px wide */
  @media (min-width: 640px) {
    columns: 2;
    gap: 16px;
  }
}
```

Media queries have served front-end developers well but they do have limitations. In the example above, the `<article>` becomes two columns when the page is more than 640 pixels wide, but this has no context of the rest of the page. As web developers, we need to be aware of the page layout and account for padding, sidebars, ads, etc. This top-down approach is bad for code scalability.

Even worse, the media query uses pixel units. This is fine if the user’s browser font size is set to the default 16px, but could have unexpected results if they have a different size set. If only there was a way our article could be responsive to its container, so it becomes two columns if there is enough space.

## Parental guidance

Luckily for us, there is. _Container queries_ are a recent addition to CSS and work similarly to media queries. The big difference is they allow elements to be responsive to their container instead of the page. Let’s update the example.

First we need a container, so let’s wrap our `<article>` in a `<div>` with a my-container class.

```html
<div class="my-container">
  <article>
    <!-- Article content goes here -->
  </article>
</div>
```

Next, let’s change our media query to a container query. While we’re at it, lets use `em` units so the whole thing works independently of font size.

```css
.my-container {
  container: size;

  article {
    font-family: Helvetica, Arial, sans-serif;

    @container (min-width: 40em) {
      columns: 2;
      gap: 1em;
    }
  }
}
```

You can see this in action [on Codepen](https://codepen.io/liamnewmarch/pen/LYoVvJV) – note that you’ll need to use a desktop browser so you can resize the window, but notice how the article changes from one column at mobile sizes to two columns at desktop sizes. If you’re feeling adventurous, try changing your browser’s default font size and notice how the breakpoint changes accordingly.

## Parting thoughts

This is a small example of how container queries can help build accessible interfaces, and only scratches the surface of CSS containment. For more information, check out the [reference docs on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_containment).

A quick word on browser support. CSS container queries and units are available in all major browser engines, but only as of late 2023. As with all web platform features, check [caniuse.com](https://caniuse.com/css-container-queries) to see if it meets your project’s browser support requirements before starting work.
