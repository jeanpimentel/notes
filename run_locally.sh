#!/bin/sh

# deps
python -m pip install -r requirements.txt

# set docs
if [ ! -d "docs" ]; then
	git clone $(git config --get remote.origin.url) docs
else
	cd docs && git pull && cd ..
fi

# build
mkdocs serve
