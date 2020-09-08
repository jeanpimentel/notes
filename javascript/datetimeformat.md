# DateTimeFormat



We are trying to remove a lot of _unnecessary_ dependencies from our project. One of the libraries is _moment.js_

You can find good options here: [https://github.com/you-dont-need/You-Dont-Need-Momentjs](https://github.com/you-dont-need/You-Dont-Need-Momentjs)



Common scenarios:

```javascript
> const now = new Date('2020-09-02T16:07:55+00:00');
> now
Wed Sep 02 2020 13:07:55 GMT-0300 (Brasilia Standard Time)
```

```javascript
> Intl.DateTimeFormat('en-US').format(now)
"9/2/2020"

> Intl.DateTimeFormat('en-US', { dateStyle: "full" }).format(now)
"Wednesday, September 2, 2020"

> Intl.DateTimeFormat('en-US', { dateStyle: "long" }).format(now)
"September 2, 2020"

> Intl.DateTimeFormat('en-US', { dateStyle: "medium" }).format(now)
"Sep 2, 2020"

> Intl.DateTimeFormat('en-US', { dateStyle: "short" }).format(now)
"9/2/20"
```



Documentation is available here: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DateTimeFormat)