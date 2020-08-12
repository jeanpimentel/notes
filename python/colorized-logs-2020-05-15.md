# Colorized logs

Without changing the code


## Installation
The coloredlogs package is available on PyPI which means installation should be as simple as:

```shell
pip install coloredlogs
```

## Setup

You can set everything on code, but I'm not using it because I don't want to introduce a new dependency. 
So, there is a MAGIC way:

```shell
export COLOREDLOGS_AUTO_INSTALL=1
export COLOREDLOGS_LOG_FORMAT='%(asctime)s %(name)s %(levelname)s %(message)s'
export COLOREDLOGS_DATE_FORMAT='%H:%M:%S'
export COLOREDLOGS_FIELD_STYLES='asctime=green;name=magenta;levelname=white,bold'
make run # or flask run, yarn start etc
```
