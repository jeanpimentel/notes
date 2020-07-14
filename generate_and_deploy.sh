#!/bin/sh

# deps
python -m pip install -r requirements.txt

# set docs
git clone $(git config --get remote.origin.url) docs

# pre-build
echo "notes.jeanpimentel.dev" > docs/CNAME

# build
mkdocs gh-deploy --force
