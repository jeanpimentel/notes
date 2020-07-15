# NSDataDetector

@available(iOS 4.0, *)

- Subclasse de *NSRegularExpression*
- Detecta vários tipos de dados:
  - Datas, endereços, links, telefones...
- Apresenta boa precisão



## NSTextCheckingType.Link

```swift
let text = "Veja mais em: http://developer.apple.com/"

let detector = try NSDataDetector(types: NSTextCheckingType.Link.rawValue)

let match = detector.firstMatchInString(text, options: [], range: NSRange(location: 0, length: text.utf16.count))

print(match?.URL)
// Optional(http://developer.apple.com/)
```



## NSTextCheckingType.Address

```swift
let text = "Av dos Andradas, Belo Horizonte, MG - 30260-070"

let detector = try NSDataDetector(types: NSTextCheckingType.Address.rawValue)

let match = detector.firstMatchInString(text, options: [], range: NSRange(location: 0, length: text.utf16.count))

print(match?.addressComponents)
// Optional(["ZIP": "30260-070", "City": "Belo Horizonte", "State": "MG", "Street": "Av dos Andradas"])
```



## Chega de REGEXES malucas para validar email

```swift
let text = "contato@jeanpimentel.com.br"

let detector = try NSDataDetector(types: NSTextCheckingType.Link.rawValue)

let match = detector.firstMatchInString(text, options: [], range: NSRange(location: 0, length: text.utf16.count))

print(match?.URL)
// Optional(mailto:contato@jeanpimentel.com.br)
```



### Exemplo com extension

```swift
extension String	 {

    func isEmail() -> Bool {

        guard let detector = NSDataDetector(types: NSTextCheckingType.Link.rawValue) else { return false }
        
        let match = detector.firstMatchInString(self, options: [], range: NSRange(location: 0, length: self.utf16.count))

        return match?.URL?.scheme == "mailto"
    }
}
```



### Resultado

```swift
print("josé@email.com".isEmail())
// true

print("ашка@ящик.рф".isEmail())
// true
```

