# A Jupyter notebook demonstrating the Bitcoin Test Framework #

## Setup ##

### OSX ###
```
$ brew install bitcoin
$ brew services start bitcoin
```
(more complicated instructions to build from source [here](https://github.com/bitcoin/bitcoin/blob/master/doc/build-osx.md))

### Ubuntu ###
TODO

### Install Dependencies ###

Create and activate your virtual environment (not strictly required):
```
$ python3 -m virtualenv .venv3 && virtualenv .venv3/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

## Fire up Jupyter notebook to see exercises ##
```
$ jupyter-notebook
```
