# Low Power Mode

@available(iOS 9.0, *)


- Modo de economia de bateria
- iOS reduz processamentos, brilho da tela, requisições em background etc
- Informação pode ser obtida diretamente ou via NotificationCenter


```swift
if NSProcessInfo.processInfo().lowPowerModeEnabled {
	// evitar autoplay em vídeos
	// diminuir atualização do GPS
	// evitar requisições de rede
	// etc
} else {
//
}
```

```swift
NSNotificationCenter.defaultCenter().addObserver(
	self,
	selector: #selector(callMe),
	name: NSProcessInfoPowerStateDidChangeNotification,
	object: nil
)
```