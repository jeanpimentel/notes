# UIImageView.transitionWithView

@available(iOS 4.0, *)

```swift
label.text = "😃"

// ...
UIView.transitionWithView(label, 
	duration: 0.5,
	options: .TransformationFlipFromLeft,
	animations: {
		label.text = "😨"
	},
	completion: nil
)
```

![](./uiimageview-transition1.gif)

---

```swift
imageView.image = UIImage(named:"empty")

// ...
UIView.transitionWithView(imageView, 
	duration: 0.5,
	options: .TransformationCrossDisolve,
	animations: {
		imageView.image = UIImage(named:"full")
	},
	completion: nil
)
```

![](./uiimageview-transition2.gif)



