# fondy

Fondy.eu Python SDK

## Install

```
pip install fondy
```

## Usage example

```python
from fondy import API
fondy = API(merchant_id, password, key)
fondy.invoice('20.00', 'UAH')
```
