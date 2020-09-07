# Generate file extensions db

## Overview

This generates a json that contains all the file extensions shown on the site [fileinfo.com](https://fileinfo.com) by scanning it.

The result `.json` look like this

```json
[
    {
        "filetype": ".!bt",
        "developer": "BitTorrent",
        "category": "Misc Files",
        "format": "Text and Binary"
    },
    ...
]
```

[TOC]

## Platform

Implemented in python.
As Python is cross-platform, it can be run on Windows, Linux-based or Mac systems. The only thing you need to have installed is `python3`.

## Dependencies

The dependencies are in the `requirements.txt` file.

If you use `virtualenv` you need to create/activate it first.
Them, you can install the dependencies using `pip` as follows:

```bash
pip install -r requirements.txt
```

> NOTE: We recommend use `venv` to your python projects.

## How to use

If the only thing that you want to do is generate the filetype database, you have to open a **console** from the folder project and make

```bash
python3 main.py
```

assuming that you have the `python` installation in the PATH environment variable, if not, replace `python3` for the path of the python executable.
