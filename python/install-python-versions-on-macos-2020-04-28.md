# Install python versions on macOS

1. you need pyenv

```shell
brew install pyenv
```

2. add pyenv path

```shell
echo 'export PATH="$(pyenv root)/shims:$PATH"' >> ~/.zshrc
```

3. install python version

```shell
pyenv install --list | grep 3.X.Y
```

```shell
pyenv install 3.X.Y
python-build: use openssl@1.1 from homebrew
python-build: use readline from homebrew
Downloading Python-3.X.Y.tar.xz...
-> https://www.python.org/ftp/python/3.X.Y/Python-3.X.Y.tar.xz
Installing Python-3.X.Y...
python-build: use readline from homebrew
python-build: use zlib from xcode sdk
Installed Python-3.X.Y to /Users/<user>/.pyenv/versions/3.X.Y
```

4. list installed python versions

```shell
pyenv versions
```

5. if you want to change the default version

```shell
pyenv global 3.X.Y
```

Source:
[https://installvirtual.com/how-to-install-python-3-8-on-mac-using-pyenv/](https://installvirtual.com/how-to-install-python-3-8-on-mac-using-pyenv/)
