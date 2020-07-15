# JavaScriptCore

@available(iOS 7.0, *)



Wrapper no motor JavaScript do WebKit



JSContext, equivalente à window

JSValue, tipo dinâmico, faz a tradução



É o que torna o **ReactNative** possível 



```swift
let context = JSContext()

context.evaluateScript("var sum = 1 + 2")

context.evaluateScript("var double = function(value) {
	return value * 2 
}")

let result: JSValue = context.evaluateScript("double(sum)")
   
print(result.toInt32())
// 6
```

```swift
context.evaluateScript("var names = ['jean', 'luiz']")

let names = context.objectForKeyedSubscript("names")

let firstName = names.objectAtIndexedSubscript(0)

print(firstName.toString())
// jean
```

```swift
context.evaluateScript("var double = function(value) {
	return value * 2 
}")

// ...

let double = context.objectForKeyedSubscript("double")

let result = double.callWithArguments([5])

print(result.toInt32())
// 10
```

```swift
context.exceptionHandler = { context, exception in
	print(exception)
}

// ...

context.evaluateScript("var double = function(value) { return value * }")
// SyntaxError: Unexpected token '}'
```