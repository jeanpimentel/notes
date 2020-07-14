# Console.log and more

### console.log

You don't need to concatenate values

```diff
const name = "Jean";
-console.log('name: ' + name); // DON'T
+console.log('name:', name); // DO
``` 


### console.count([label])

```js
function MyComponent(props) {
	console.count('Rendering...');
	...
}
```


```js
Rendering: 1
Rendering: 2
Rendering: 3
Rendering: n
```

### console.table(data [, columns])

```js
const elements = ['H', 'He', 'Li']
console.table(elements)
```

| (index) | Values |
|---------|--------|
| 0       | "H"    |
| 1       | "He"   |
| 2       | "Li"   |


```js
const elements = [
  {
    number: 1,
    symbol: "H",
    name: "Hydrogen",
  },
  {
    number: 2,
    symbol: "He",
    name: "Helium",
  }
 ]
```

```js
console.table(elements[0])
```

| (index) | Value     |
|---------|-----------|
| number  | 1         |
| symbol  | "H"       |
| name    | "Hydrogen |


```js
console.table(elements)
```

| (index) | number | symbol | name     |
|---------|--------|--------|----------|
| 0       | 1      | "H"    | Hydrogen |
| 1       | 2      | "He"   | Helium   | 


```js
console.table(elements, ["number", "name"])
```

| (index) | number | name     |
|---------|--------|----------|
| 0       | 1      | Hydrogen |
| 1       | 2      | Helium   | 


Source: [https://developer.mozilla.org/en-US/docs/Web/API/Console](https://developer.mozilla.org/en-US/docs/Web/API/Console)
