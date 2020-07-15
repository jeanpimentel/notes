# Acessibilidade 101

---

*Os slides estão disponíveis aqui: [https://speakerdeck.com/jeanpimentel/acessibilidade-no-android-101-google-io-extended-2017
](https://speakerdeck.com/jeanpimentel/acessibilidade-no-android-101-google-io-extended-2017)*

---

__Usabilidade__

> "Rapidez com que os utilizadores podem aprender a usar alguma coisa, a eficiência deles ao usá-la, o quanto se lembram daquilo, o grau de propensão a erros e o quanto gostam de utilizá-la" - Jakob Nielsen

__Acessibilidade__

> "Possibilidade e condição de alcance para utilização, com segurança e autonomia, de espaços, […] informação e comunicação, […] por pessoa com deficiência ou com mobilidade reduzida;" - Lei 10.098/2000


### Usabilidade + Acessibilidade: 

__Design Universal__: tudo pode ser usado por todos, independente de idade, habilidade ou situação.



### Deficiências

- **1 bilhão** de pessoas com alguma forma de deficiência
- 80% dessas pessoas residem em países em desenvolvimento

*Fonte: Organização Mundial da Saúde, 2011*


### Deficiências - Brasil

- **45 milhões** de brasileiros com alguma forma de deficiência
- 85% vivem em áreas urbanas

- **18.6% - Visual**
- 7.0% - Motora
- 5.1% - Auditiva
- 1.4% - Mental/Intelectual

*Fonte: IBGE, 2010*


### Deficiências

- Cegueira
- Daltonismo
- Hipermetropia
- Parkinson
- Imobilização
- Mãos ocupadas
- Surdez
- Mudez
- ...


### Mitos

- Se eu consigo, todo mundo consegue
- Difícil de implementar
- Consome muito tempo e dinheiro
- É responsabilidade dos desenvolvedores


### Resolva problemas reais

Não assuma que:

- sua equipe sabe os problemas
- sua equipe pensou em tudo
- seus usuários se comportam como você espera


### Personas

Personagens ficcionais criados para representar os diferentes grupos de usuários que irão interagir com um app, produto, serviço etc.

Ajudam o time a entender quem é o consumidor, quais suas características, desejos, necessidades, preocupações e objetivos.


### Personas: José de Souza

- 65 anos
- Aposentado
- Visão ruim, tremor nas mãos e memória curta
- Prefere textos largos, imagens e ícones chamativos
- Se perde facilmente durante a navegação
- Usa o telefone com letras grandes, somente para ligar para parentes e ver as fotos dos netos


## Limitações


### Visão: cegos

- Não podem escanear o conteúdo
- Difícil de acessar informações visuais
- Limitado pelos leitores de telas


### Visão: baixa visão

- Glaucoma, catarata, hipermetropia… 
- Não conseguem ler textos pequenos sem a lupa
- Textos em imagens são difíceis de ler
- Baixo contraste e resolução dificultam muito


### Visão: daltônicos

- 8% da população masculina (1/12)
- Variados tipos
- Baixo contraste é péssimo
- Problemas para ler gráficos


### Audição

- Alertas sonoros devem possuir alternativas
- Áudios devem possuir transcrições
- Vídeos devem possuir legendas


### Mobilidade

- Não conseguem usar o touchscreen
- Se cansam facilmente
- Precisam de botões extras ou teclados


## Serviços do Android

- Talkback
- Brailleback
- Switch Access
- Voice Access
 

## E como fazer?


### Cor

Daltonismo: **Developer Options** > **Simulate color space**


### Contraste

Relação de contraste recomendada pela WCAG (Web Content Accessibility Guidelines).

Quanto maior a diferença, maior o contraste.

- **4.5:1 AA**
- **7:1 AAA**

Exemplos:

- texto #999 no fundo branco #fff: 2.8 👎 
- texto #777 no fundo branco #fff: 4.5 👍
- texto #555 no fundo branco #fff: 7.5 👏


### Área mínima de toque

**48dp**, aproximadamente 9mm 

Dica: `android:minHeight`, `android:minWidth`

Apesar de não recomendado, é possível aumentar a área de toque programaticamente com o uso de `TouchDelegate`


### Fontes

Sempre use dimensões em **sp (scale-independent)**

Layouts devem ser responsivos

Altere o tamanho da fonte nas configurações do dispositivo e teste


### Content Description

Semelhante ao ALT do HTML, é um texto descritivo para os elementos: `ImageButton`, `ImageView`, `Checkbox`

Se o elemento for apenas decorativo, use **@null**

```xml
<ImageView
    ...
    android:contentDescription="@null"
    android:src="@drawable/ic_music_note" />
```

Não se esqueça dos elementos dinâmicos:

```java
private void updateImageButton() {
    if (playing) {
       playPauseImageButton.setImageResource(R.drawable.ic_pause);
       playPauseImageButton.setContentDescription(getString(R.string.pause));
    } else {
       playPauseImageButton.setImageResource(R.drawable.ic_play);
       playPauseImageButton.setContentDescription(getString(R.string.play));
    }
}
```


### EditText 

- **android:labelFor** no `TextView`
- **android:hint** no `EditText`

```xml
<TextView 
    android:labelFor="@+id/email"
    android:text="@string/email" … />
<EditText
    android:id="@+id/email"
    android:hint="@string/email" … />
```


### Live Region

Usado para alterações dinâmicas, sem que seja necessário o foco. 

Faz com que o TalkBack anuncie as mudanças.

Opções: `none`, `polite`, `assertive`

```xml
<TextView
    android:id="@+id/status"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:accessibilityLiveRegion="polite" />
```


### Agrupamento de conteúdo

Evitar que o Talkback anuncie os conteúdos separadamente:
**android:focusable** + `ViewGroups`

```xml
<RelativeLayout
    android:id="@+id/song_container"
    android:focusable="true">
    <TextView
        android:id="@+id/label_song_name"
        android:text="Name" />
    <TextView
        android:id="@+id/value_song_name"
        android:text="Hey Jude" />
```


### Ordenação do Foco

Suporte a navegação por teclados externos.

- **android:nextFocusForward (Next)**
- **android:nextFocusUp**
- **android:nextFocusDown**
- **android:nextFocusLeft**
- **android:nextFocusRight**


### Atenção: CustomViews

Podem ser problemáticas!

É responsabilidade do desenvolvedor:

- Tratar navegação via teclado
- Implementar as APIs de acessibilidade
- Popular, tratar e lançar eventos: CLICKED, FOCUSED, SCROLLED… 


## Faça testes

- Android Lint
- Accessibility Scanner
- Talkback
- Voice Access
- Color Simulation
- **USUÁRIOS REAIS!**
