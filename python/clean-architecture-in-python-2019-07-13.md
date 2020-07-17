# Clean Architecture in Python



@brandon_rhodes

PyOhio 2014

Source: https://www.youtube.com/watch?v=DJtef410XaM



---



⚠️ We programmers spontaneously use subroutines **backwards**

Example:

```python
# Listing 1
import requests
from urllib import urlencode

def find_definition(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/?'
    url += urlencode({'q': q, 'format': 'json'})
    response = requests.get(url)     # I/O
    data = response.json()           # I/O
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word')
    return definition
```

```python
# Listing 2
def find_definition(word):           
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/?'
    url += urlencode({'q': q, 'format': 'json'})
    data = call_json_api(url)
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word')
    return definition

def call_json_api(url):
    response = requests.get(url)     # I/O
    data = response.json()           # I/O
    return data
```

We have *hidden* I/O, but have we really **decoupled** it?



## How we should do:

```python
# Listing 3
def find_definition(word):           
    url = build_url(word)
    data = requests.get(url).json()  # I/O
    return pluck_definition(data)

def build_url(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/?'
    url += urlencode({'q': q, 'format': 'json'})
    return url

def pluck_definition(data):
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word')
    return definition
```

`Listing 3` is an *architectural success* while the others were **failures**

`Listing 3` shows in *miniature* what the Clean Architecture does for entire applications

*Eminently readable* because it remains at a **single level of abstraction**

These names *document* what each section of code is doing



## Architecture

`Listing 1`: procedure

`Listing 2`: procedure => i/o subrotine (but top level code stills a procedure)

`Listing 3`: procedure => **pure function** + **pure function** = **TESTING!!! 👍**



## Testing Listing 1 or Listing 2

1. Dependency Injection

2. Mocks



- Dependency Injection

```python
def find_definition(word, requests=requests):
```

```python
class FakeRequestsLibrary(object):
    def get(self, url):
        self.url = url
        return self
    def json(self):
        return self.data

def test_find_definition():
    fake = FakeRequestsLibrary()
    fake.data = {u'Definition': 'abc'}
    definition = find_definition('testword', requests=fake)
```

1. Your mock is **not the real library**

2. This might look simple for *one service*

3. But a procedure that also needs a **database** and **filesystem** will need *lots* of injection

   > A high-level function needs *every single* service required by its subroutines



* Mocks

```python
from mock import patch

def test_find_definition():
    fake = FakeRequestsLibrary()
    fake.data = {u'Definition': u'abc'}

    with patch('requests.get', fake.get):
        definition = find_definition('testword')

    assert definition == 'abc'
    assert fake.url == (
        'http://api.duckduckgo.com/'
        '?q=define+testword&format=json')
```



**DI** or **patch()**

Either way, *awkward sad* 😢

Seems we are fighting with our application



## How does testing improve when we factor out our logic as in Listing 3?

```python
# Listing 3
def find_definition(word):           
    url = build_url(word)
    data = requests.get(url).json()  # I/O
    return pluck_definition(data)

def build_url(word):
    q = 'define ' + word
    url = 'http://api.duckduckgo.com/?'
    url += urlencode({'q': q, 'format': 'json'})
    return url

def pluck_definition(data):
    definition = data[u'Definition']
    if definition == u'':
        raise ValueError('that is not a word')
    return definition
```



By definition, *pure functions* can be tested using **only data**

```python
def test_build_url():
    assert build_url('word') == 'http://api.duckduckgo.com/?q=define+word&format=json'

def test_build_url_with_punctuation():
    assert build_url('what?!') == 'http://api.duckduckgo.com/?q=define+what%3F%21&format=json'

def test_build_url_with_hyphen():
    assert build_url('hyphen-ate') == 'http://api.duckduckgo.com/?q=define+hyphen-ate&format=json'
    
def test_pluck_definition():
    assert pluck_definition({u'Definition': u'something'}) == 'something'

def test_pluck_definition_missing():
    with pytest.raises(ValueError):
        pluck_definition({u'Definition': u''})
```

- **No** special set-up

- **No** special preparation

- Test calls are *symmetric* with normal calls



### A symptom of coupling: having lot of permutations

```
call_test(good_url, good_data)

call_test(bad_url1, whatever)
call_test(bad_url2, whatever)
call_test(bad_url3, whatever)

call_test(good_url, bad_data1)
call_test(good_url, bad_data2)
call_test(good_url, bad_data3)
```



## Clean Architecture

Top level = IO, bottom level = pure functions

- 1st level - Frameworks and Drives: Devices, Web, DB, External Interfaces, UI

- 2nd level - Interface Adapters: Controllers, Gateways, Presenters

- 3rd level - Application Business Rules - Use Cases

- 4th level - Enterprise Business Rules - Entities

  

> In general, the *further in* you go, the **higher level** the software becomes. The *outer circles* are mechanisms. The *inner circles* are policies.
>
> The important thing is that *isolated,* *simple* data structures are passed across the boundaries.
>
>  When any of the *external parts* of the system become **obsolete,** like the database, or the web framework, you can **replace** those obsolete elements with a minimum of fuss.



## Functional programming

LISP, Haskell, Clojure, F#

Functional languages *naturally* lead you to process data structures while avoiding **side-effect I/O**

```python
# I/O as a side effect
def uppercase_words(wordlist):
    for word in wordlist:
        word = word.upper()
        print word
```

```python
# Logic with zero side-effects
def process_words(wordlist):
    for word in wordlist:
        yield word.upper()

# I/O goes outside of logic
def procedural_glue(wordlist):
    for word in process_words(wordlist):
        print word
```

**Procedural code:** Output as-you-go

**Functional code:** Stages that each produce data, that gets output at the end



*Why functional?* Because of **immutability?**

The biggest advantage of data in a functional programming style is *not* its immutability

 **It is simply the fact that it is data!**



## 1986
McIlroy **vs.** Knuth

“Given a text file and an integer *k,* print the *k* **most common** words in the file (and the number of their occurrences) in **decreasing frequency.**”

Knuth: **10 pages of Pascal**

McIlroy: **6-line shell script**

```bash
tr -cs A-Za-z '\n' |
tr A-Z a-z |
sort |
uniq -c |
sort -rn |
sed ${1}q
```

Traditional lesson: Use small simple tools that can easily be linked together

But I want to draw a different lesson: **The shell script is simpler because it operates through the stepwise transformation of data**



## Real world examples

- Skyfield https://rhodesmill.org/skyfield/

  **Object-based** API backed by dozens of *pure functions* that implement the actual operations

  The **miserable** thing about a method is that it *implicitly* depends upon the state of the whole object

  The **beautiful** thing about a function is that it *explicitly* depends upon a specific list of arguments



- Luca https://github.com/brandon-rhodes/luca

  - **Temptation**: Compute *output* fields as the form is running, *writing*their text into the PDF
  - **Instead: phases**
    - First read the entire tax form
    - Then do all the computations
    - Finally write to the PDF



## Wrap-up

**Old:** To get rid of I/O, make it subordinate

**New: **To *really* get rid of someone, make them a *manager!*



Wheeler: In 1952 he gave us the `sub-routine`

*We have yet to realize its full power and promise!*



When a programme has been made from a set of **sub-routines** the breakdown of the code is **more complete** than it otherwise would be.

This allows the coder to concentrate on **one section** of the program at a time without the overall detailed programme **continually intruding**.

Thus the sub-routines can be **more easily** coded and be **tested** in isolation from the rest of the programme.

When the **entire programme** has to be tested it is with the foreknowledge that the **incidence of mistakes** in the subroutine is — *zero*

(or at least **one order of magnitude** below that of the **untested** portions of the programme!)

