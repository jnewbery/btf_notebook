# A Jupyter notebook demonstrating the Bitcoin Test Framework #

## Warning ##

Do not run test instances of bitcoind on the same machine that you store your Bitcoin private keys. This test framework shouldn't interfere with your standard bitcoind directory, but why risk it?

## Setup ##

It is recommended to build bitcoin directly from source (or use signed binaries) to minimize trust in third parties. However, these steps are much easier.

### OSX ###
Install using [Homebrew](https://brew.sh/):
```
$ brew install bitcoin && brew services start bitcoin
```
(more complicated instructions to build from source [here](https://github.com/bitcoin/bitcoin/blob/master/doc/build-osx.md))

### Ubuntu ###
Install using [Launchpad](https://launchpad.net/~bitcoin/+archive/ubuntu/bitcoin)
```
$ sudo add-apt-repository ppa:bitcoin/bitcoin && sudo apt-get update
```
(more complicated instructions to build from source [here](https://github.com/bitcoin/bitcoin/blob/master/doc/build-unix.md))

### Install Dependencies ###

Create and activate your virtual environment (not strictly required):
```
$ python3 -m venv .venv3 && source .venv3/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

## Fire up Jupyter notebook to see exercises ##
```
$ jupyter-notebook
```
