# String Transform

Antigo `CFStringTransform`

@available(iOS 9.0, *)



```swift
let text = "🍕".stringByApplyingTransform(NSStringTransformToUnicodeName, reverse: false)

print(text)
// {SLICE OF PIZZA}
```

```swift
let text = "Luna".stringByApplyingTransform(NSStringTransformLatinToCyrillic, reverse: false)

print(text)
// Луна
```

```swift
let text = "您好".stringByApplyingTransform(NSStringTransformMandarinToLatin, reverse: false)

print(text)
// nín hǎo
```

```swift
let text = 
	"您好"
		.stringByApplyingTransform(NSStringTransformMandarinToLatin, reverse: false)
		.stringByApplyingTransform(NSStringTransformStripDiacritics, reverse: false)

print(text)
// nin hao
```

```swift
let text = "Αθήνα".stringByApplyingTransform("Any-Latin; Latin-ASCII; Lower", reverse: false)

print(text)
// athena
```

