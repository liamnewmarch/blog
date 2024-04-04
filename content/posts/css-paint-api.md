---
date: 2018-05-30
title: An introduction to the CSS Paint API
summary: Explore the CSS Paint API, a Houdini spec which allows you to define new paint behaviours.
---

A few years ago there were rumblings about a specification coming to CSS nicknamed _Houdini_. [First described](https://www.smashingmagazine.com/2016/03/houdini-maybe-the-most-exciting-development-in-css-youve-never-heard-of/) as a way of writing polyfills for CSS, Houdini is a [suite of APIs](https://drafts.css-houdini.org/) which give developers programmatic control over layout, paint, animation and more.

In this article we’ll explore the CSS Paint API, a Houdini spec which allows you to define new paint behaviours. We’ll also have a quick look at the new CSS Typed Object Model (or CSS Typed OM), also part of Houdini, which can be used with [Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables) to great effect.

Before we get into it I should mention browser support. At the time of writing [Chrome is the only browser](https://ishoudinireadyyet.com/) that supports these technologies, however there is a polyfill for both the [CSS Paint API](https://github.com/GoogleChromeLabs/css-paint-polyfill) and [CSS Typed OM](https://github.com/csstools/css-typed-om). Hurrah! Now, what _are_ they?

## The CSS Paint API

The [CSS Paint API](https://www.w3.org/TR/css-paint-api-1/) is an exciting new bit of kit which gives you the ability to use [CanvasRenderingContext2D](https://developer.mozilla.org/en/docs/Web/API/CanvasRenderingContext2D) in places you would normally use an image in CSS. Essentially it turns any element’s `background-image` into a `<canvas>`.

The original [Google Developers Houdini](https://developers.google.com/web/updates/2016/05/houdini) post from 2016 is a little out-of-sync with the spec now, for instance the APIs have moved under the `window.CSS` global object, but the core concepts are the same. Like other Houdini APIs, the Paint API is built on the concept of _worklets_.

[Worklets](https://developer.mozilla.org/en-US/docs/Web/API/Worklet) are small scripts that are similar to [Workers](https://developer.mozilla.org/en-US/docs/Web/API/Worker), but with some differences. Where workers are long-lived and designed to run computationally expensive work off the main thread, worklets are purposefully lightweight for running smaller operations multiple times per frame, not unlike [shaders](https://en.wikipedia.org/wiki/Shader).

Here’s a very simple example where we use a paint worklet to paint the background of an element blue:

```html
<!DOCTYPE html>
<style>
  .hello-world {
    background-image: paint(hello-world);
    height: 200px;
    width: 300px;
  }
</style>
<div class="hello-world"></div>
<script>
  CSS.paintWorklet.addModule('hello-world.js');
</script>
```

And in `hello-world.js` (our worklet):

```js
class HelloWorld {
  paint(context, geometry) {
    context.fillStyle = 'blue';
    context.fillRect(0, 0, geometry.width, geometry.height);
  }
}

registerPaint('hello-world', HelloWorld);
```

Notice that we’re defining a class with one method, `paint()`. The first argument passed to it is a 2D canvas-like context and the second gives the geometry of the element being painted. The `paint()` method will run every time the geometry changes, most often when a resize occurs.

Lets make this a little bit more interesting by adding some theming support with Custom Properties and the CSS Typed OM.

## CSS Typed Object Model

The interface between CSS and JavaScript has been lacking for some time. CSS has a [complex type system](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Types) which can represent values ranging from lengths, angles, durations and frequencies to functions like colours, shapes, timings and transformations, but despite this the main way we interact with these values in JavaScript is by passing and parsing strings.

The [CSS Typed OM](https://www.w3.org/TR/css-typed-om-1/) aims to fix that by providing hooks for creating and manipulating CSS values in JavaScript. Values can be created by using methods on the `window.CSS` global, for example `CSS.px(20)` returns a CSSUnitValue — an object with a `unit` and `value` property, which when cast to a string gives `"20px"`. The model also gives every element an `attributeStyleMap` property and `computedStyleMap()` method which accept these new types:

```js
const div = document.createElement('div');
div.attributeStyleMap.set('margin-top', CSS.px(20));
```

Similarly, you can `get` properties like so:

```js
const property = div.attributeStyleMap.get('margin-top');
property.value === 20; // true
property.unit === 'px'; // true
```

There is so much more to the Typed OM than this simple example — I highly recommend reading “[Working with the new CSS Typed Object Model](https://developers.google.com/web/updates/2018/03/cssom)” on Google Developers — but the _really_ cool thing it gives you is the ability to register definitions for new properties.

Lets define two new properties for our `hello-world` example using the new `CSS.registerProperty()` method, `--background-color` and `--background-padding` which we’ll register as a `<color>` and `<length>` types respectively.

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      .hello-world {
        --background-color: red;
        --background-padding: 1em;
        background-image: paint(hello-world);
        border: 1px solid black;
        height: 200px;
        width: 300px;
      }
    </style>
    <script>
      CSS.registerProperty({
        name: '--background-color',
        syntax: '<color>',
        initialValue: 'blue',
        inherits: false,
      });

      CSS.registerProperty({
        name: '--background-padding',
        syntax: '<length>',
        initialValue: 0,
        inherits: false,
      });

      CSS.paintWorklet.addModule('hello-world.js');
    </script>
  </head>
  <body>
    <div class="hello-world"></div>
  </body>
</html>
```

There are a few options you can pass to `registerProperty()`. You can add an `initialValue` to specify a default in the event that the property is missing (or invalid), and the `inherits` boolean tells the parser whether or not values are inherited from the element’s parent. The `syntax` key is the most complicated however, and is used to tell the parser which CSS type(s) should be accepted as valid — [see the spec](https://www.w3.org/TR/css-properties-values-api-1/#supported-syntax-strings) for a full list of supported syntax strings.

In our worklet we need to make some modifications so the Paint API knows that we want to use our custom properties as inputs. These then become available to the `paint()` method as it’s third argument.

```js
class HelloWorld {
  static get inputProperties() {
    return [
      '--background-color',
      '--background-padding',
    ];
  }

  paint(context, geometry, properties) {
    const color = properties.get('--background-color').value;
    const padding = properties.get('--background-padding').value;
    const height = geometry.height - padding * 2;
    const width = geometry.width - padding * 2;
    context.fillStyle = color;
    context.fillRect(padding, padding, width, height);
  }
}

registerPaint('hello-world', HelloWorld);
```

Notice that even though in the `--background-padding` is specified in `em` units, the Typed OM converts this to `px` by default so we can use it directly in our paint context without having to convert it ourselves. If you’re using Chrome you can see the final result here:

[Live demo on GitHub.](https://liamnewmarch.github.io/css-paint-api-demo/)

Try playing with the values of `--background-color` and `--background-padding` in DevTools and notice that the changes are reflected immediately just like ‘real’ CSS properties.

## Summary

This is just the beginning for Houdini. In addition to painting, there are APIs in the works for layout and animation, and worklets have been incorporated into the Web Audio API.
The demos in this article only scratch the surface when it comes to the power of the Paint API and the Typed OM. Although they’re only implemented in one browser so far, I’m excited to have the option of using these features for progressively enhancement. In the meantime, you can track adoption by other browser vendors at [ishoudinireadyyet.com](https://ishoudinireadyyet.com/).
