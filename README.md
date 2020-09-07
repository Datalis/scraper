# Scrapers

On the main branch *master* they are a base scraper to scan websites.
Each other branch, is an scraper with specific purpose.



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

Define your own scrapers by inherit from the `Scraper` class, it provide some useful functionalities.
