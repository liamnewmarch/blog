---
date: 2014-07-14
title: An introduction to Promises in JavaScript
summary: Learn how Promises work by building a simple script loader
---

Promises are making a big splash in the JavaScript world. They are a way of handling _asynchronous logic_ in a way that avoids nested callbacks. In this post I hope to explain why Promises are useful, and how you can start using them today.


## Browser support

Promises are being finalised as part of the latest and greatest version of JavaScript called ECMASCript 6 (or ES6 if you’re cool). Native browser support isn’t great but there is out of the box support in Chrome 32+ and Firefox 29+.

For projects that _have to_ run on other browsers Jake Archibald has you covered with the [ES6 Promise](https://github.com/jakearchibald/es6-promise) polyfill. Include it on a page and you can use the proper ES6 Promise syntax on old devices. Beautiful.


## Before Promises

Okay, so what do I mean by _asynchronous logic_? I’m talking about a function call that sets up a listener or callback for something that will happen in the future.

This could be anything that takes time. We could be waiting for the DOM to load, AJAX requests to return, animations to complete, timers to finish, even user interaction. In short, anything that we would use a callback function for.

Traditional JavaScript callbacks work very well up to a point, but we run into problems when we're waiting for multiple conditions to be met. Anyone who has used Node.js will be familiar with the concept of callback hell:

```js
waitForConditionOne(function() {
  waitForConditionTwo(function() {
    waitForConditionThree(function() {
      waitForConditionFour(function() {
        waitForConditionFive(function() {
          // All conditions are met, run my code now
        });
      });
    });
  });
});
```

The callback pyramid is ugly but at least it’s clear what’s happening. The ultimate goal is to maintain this level of readability without sacrificing good code style.

Better yet, what if there was a way to somehow run all of these steps in parallel, rather than waiting for each to complete in turn. But wait, there _is_ a way!


## Enter the Promise

Promises make the whole process of waiting for asynchronous events cleaner and easier by abstracting the problem. Instead of nesting our functions we convert them into Promise objects that can be chained together.

A Promise object is created by running the following:

```js
var myPromise = new Promise(function(resolve, reject) {
  // Our condition here
});
```

A Promise object can exist in one of three states; _pending_, _resolved_, or _rejected_. Since our Promise doesn’t do anything, `myPromise` is _pending_.

The arguments supplied to our anonymous function, `resolve` and `reject` are functions. The idea is to use these to change the state of our Promise when the asynchronous operation is complete. Let’s look at some code.

In this example we’ll use `setTimeout` to wait three seconds before resolving `myPromise` with the string `'Hello, world!'`:

```js
var myPromise = new Promise(function(resolve, reject) {
  // Wait three seconds before resolving
  setTimeout(function() {
    resolve('Hello, world');
  }, 3000)
});
```

This works, but it doesn’t do very much. `myPromise` changes state but we need to specify what happens when the promise is resolved. To do this we pass a function to the `then` method of `myPromise`:

```js
var myPromise = new Promise(function(resolve, reject) {
  setTimeout(function() {
    resolve('Hello, world');
  }, 3000)
});

// Do something when the promise gets resolved
myPromise.then(function(value) {
  console.log(value);
});
```

The beauty of using Promises is that we can add multiple `then` methods, and at any point.

In the example above we could call `myPromise.then` many times with different callback functions and each will be called. It also doesn’t matter what state the Promise is when we add a `then`. If the Promise is _pending_ the new callback will be added to the queue; if it’s already _resolved_ the callback will be executed immediately.

_While the functions passed to `Promise()` are executed in a synchronous manner, functions passed to `then()` are executed on the next ‘tick’ – the equivalent of `setTimeout(..., 0)` – even if the Promise status is resolved._


## Handling rejection

As well as handling success where `resolve` is called, Promises can also handle failure with the `reject`. Lets look at how we can handle rejection with a more useful example.

Lets say we want to include an external JavaScript library in our page dynamically. In order to use the library we need to wait for it to load, which we can do by listening for it’s `load` event to fire. Here’s how that might look using Promises:

```js
function loadScript(url) {
  var scriptPromise = new Promise(function(resolve, reject) {
    // Create a new script tag
    var script = document.createElement('script');
    // Use the url argument as source attribute
    script.src = url;

    // Call resolve when it’s loaded
    script.addEventListener('load', function() {
      resolve(url);
    }, false);

    // Add it to the body
    document.body.appendChild(script);
  });

  // Return the Promise
  return scriptPromise;
}

// Load a script
loadScript('/path/to/script.js').then(function(value) {
  // Resolved
  console.log('Script loaded from:', value);
});
```

This works, but it doesn’t handle the case where the script is not found. To do this we can call the `reject` function from the Promise callback, in the same way that we call `resolve` on successful completion.

Finally, we can add a second anonymous function argument to the `then` method to specify what we do in the event of a rejection. Here’s the updated code:

```js
function loadScript(url, success, failure) {
  var scriptPromise = new Promise(function(resolve, reject) {
    // Create a new script tag
    var script = document.createElement('script');
    // Use the url argument as source attribute
    script.src = url;

    // Call resolve when it’s loaded
    script.addEventListener('load', function() {
      resolve(url);
    }, false);

    // Reject the promise if there’s an error
    script.addEventListener('error', function() {
      reject(url);
    }, false);

    // Add it to the body
    document.body.appendChild(script);
  });

  scriptPromise
}

// Load a script
loadScript('/path/to/script.js').then(function(value) {
  // Resolved
  console.log('Script loaded from:', value);
}, function(value) {
  // Rejected
  console.error('Script not found:', value)
});
```

There is a `catch` method which works similarly to the `then` method except only takes a single `rejected` callback. Use of this method is not recommended when using the ES6 Promise polyfill due to IE8 and below regarding `catch` as a reserved keyword.


## Promises in series

Awesome! So what if we want to add more than one external JavaScript library in our example? Well thanks to the fact that our `loadScript` function returns a Promise object, we can take advantage of the chainable nature of `then`.

Unless a return is specified, the `then` method will return a copy of the original Promise allowing multiple `then` callbacks to be triggered at once. This can be overridden by returning a new Promise which allows a chain of conditions to be specified in series.

Using the `loadScript` function we defined above, we can do the following:

```js
loadScript('/path/to/script-1.js').then(function() {
  return loadScript('/path/to/script-2.js');
}).then(function() {
  return loadScript('/path/to/script-3.js');
}).then(function() {
  return loadScript('/path/to/script-4.js');
}).then(function() {
  console.log('Loaded!');
});
```

This will load each script followed by our final callback, all without resorting to callback hell. If the scripts have to be loaded in strict sequence, then this is unfortunately as far as we can go. However if each script was an independent _module_ and the loading order didn’t matter, we could take things a step further. Lets assume we can.


## Going parallel

The final benefit we stand to gain from Promises is to fulfil all of our Promise requests at once. That way we can resolve all of our Promises in parallel instead of waiting for each to resolve in turn.

`Promise.all` and `Promise.race` are static methods that each take an Array of Promises as an argument, returning a new Promise. Both methods will watch the Array but with one important difference; `Promise.all` will resolve when _all_ of the Promises in the Array have resolved, whereas `Promise.race` will resolve as soon as _any one_ Promise in the Array has resolved.

Since we want to wait till all of our scripts have loaded, we need to use `Promise.all`. We need to refactor our `loadScript` function a bit to accommodate this change. For reusability I’ve chosen to rewrite it as a reusable `ScriptLoader` object.

```js
function ScriptLoader() {

  var promises = [];

  this.add = function(url) {
    var promise = new Promise(function(resolve, reject) {

      var script = document.createElement('script');
      script.src = url;

      script.addEventListener('load', function() {
        resolve(script);
      }, false);

      script.addEventListener('error', function() {
        reject(script);
      }, false);

      document.body.appendChild(script);
    });

    promises.push(promise);
  };

  this.loaded = function(callback) {
    Promise.all(promises).then(callback);
  };
}

var loader = new ScriptLoader();

loader.add('/path/to/script-1.js');
loader.add('/path/to/script-2.js');
loader.add('/path/to/script-3.js');
loader.add('/path/to/script-4.js');

loader.loaded(function(returned) {
  console.log('Loaded!');
});
```

## Wrapping up

And there we have it. If you’d like to read more about Promises and see more code examples, I highly recommend Jake Archibald’s excellent article on HTML5 Rocks called [JavaScript Promises: There and back again](http://www.html5rocks.com/en/tutorials/es6/promises/). There’s also great documentation available on the [Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), and finally the open [Promises/A+](http://promisesaplus.com/) standard itself.
