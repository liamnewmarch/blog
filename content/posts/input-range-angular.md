---
published: 2015-04-07
summary: Get a numeric value from only eleven lines of code.
title: Using range inputs with AngularJS
---

I was working on an AngularJS project recently that used HTML input sliders like this:

```html
<input type="range" ng-model="value" min="1" max="100">
```

Angular supports `number` inputs but doesn’t entirely support `range` inputs. They work for the most part; the `ng-model` binds correctly and you can use events like `ng-click` and `ng-change` fine. However, the model’s value is always a string, whereas for `number` inputs the value gets correctly coerced to a number.

Fortunately this is fairly easy to fix by using `ngModel.NgModelController` [(see the docs)](https://docs.angularjs.org/api/ng/type/ngModel.NgModelController). By requiring `ngModel` in our directive it gets passed as a fourth parameter to the `link` function. Now we can access the `$parsers` array which is used to transform the value.

Here’s a parser that coerces the value to a number:

```js
yourApp.directive('input', function() {
  return {
    restrict: 'E',
    require: '?ngModel',
    link: function(scope, element, attrs, ngModel) {
      if ('type' in attrs && attrs.type.toLowerCase() === 'range') {
        ngModel.$parsers.push(parseFloat);
      }
    }
  };
});
```

Since `parseFloat` already takes a string and returns a number we don’t even need to wrap it in a function. Pretty neat!
