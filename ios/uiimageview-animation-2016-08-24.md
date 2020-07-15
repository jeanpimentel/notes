# UIImageView.startAnimating

@available(iOS 2.0, *)

- "GIFs"
- Lista de `UIImage`, frame a frame



```swift
var images: [UIImage] = []
for i in 0..<8 {
	let name = String(format: "loading-%d", i)
	images.append(UIImage(named: name)!)
}

imageView.animationImages = images
imageView.animationDuration = 0.8
imageView.animationRepeatCount = 0

imageView.startAnimating()
```


![](./uiimageview-animation.gif)