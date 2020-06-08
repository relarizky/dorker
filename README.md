# Dorker

> Simple python based script for dorking with Google and Bing Search Engine

[![Build Status](https://travis-ci.com/relarizky/dorker.svg?branch=master)](https://travis-ci.com/relarizky/dorker)
[![license](https://img.shields.io/apm/l/vim-mode)](https://img.shields.io/apm/l/vim-mode)
[![Python version](https://img.shields.io/pypi/pyversions/django)](https://img.shields.io/pypi/pyversions/django)
[![tested os](https://img.shields.io/badge/Tested%20on-ubuntu%2019.10-critical)](https://img.shields.io/badge/Tested%20on-ubuntu%2019.10-critical)

<a href="https://asciinema.org/a/NxEZHytajAoUzmVqmSIQ6ddiU" target="_blank"><img alt="tools-preview" align="center" rc="https://asciinema.org/a/NxEZHytajAoUzmVqmSIQ6ddiU.svg"></a>

## Instalation
```
$ git clone https://github.com/relarizky/dorker.git
$ cd dorker
$ pip3 install requests
$ chmod +x dork.py
$ ./dork.py
```

## usage
```
usage: dork.py [-h] [-b | -g | -a] [-f FILE] dork

Simple python based script for dorking with Google and Bing

positional arguments:
  dork                  dork that you would like to search with

optional arguments:
  -h, --help            show this help message and exit
  -b, --bing            dorking with bing search engine
  -g, --google          dorking with google search engine
  -a, --all             dorking with both bing and google search engine
  -f FILE, --file FILE  filename you'd like to use for saving output

```
