# Cuban Shop Fetcher

Send request to the [api](http://dhayservice.cimex.com.cu:1703/api/) of http://dondehay.cimex.com.cu to fetch information related to the Cuban shops of the state.

The result is store in the json file `shops.json` in the project folder. 

It create a temp file `shops.json.temp` to save data partially to construct the final json.
Do **not** delete it manually, the application will do it when it is not longer needed.

## Json structure

The json is a list of objects, each one represent the data associate to one shop. 

```json
[
    {
        "name": "nombre",
        "x_coord": "1.0",
        "y_coord": "-3.0",
        "opening_hours": "Lun, Mar, Vie",
        "municipality": "municipio",
        "province": "provincia",
        "address": "direccion",
        "mlc": false
    },
    ...
]
```



## Platform

Implemented in python.
As Python is cross-platform, it can be run on Windows, Linux-based or Mac systems. The only thing you need to have installed is `python3`.

## Dependencies

Require `urllib3`
You can install it using `pip` as follows:

```bash
pip install urllib3
```

> NOTE: We recommend use `venv` to your python projects.

## How to use

```shell
python3 main.py
```

