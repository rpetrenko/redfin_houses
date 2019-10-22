# redfin_houses
Python library to retrieve house information from Redfin.

## Setup and install
```
python -m venv venv
. venv/bin/activate
python setup.py build
python setup.py install
```

## How to use

### Example 1
* this example illustrates how to get all the properties within a 95111 zipcode and apply the following filter
    * property type = house
    * max price = 800k

```bash
python examples/example1.py
```