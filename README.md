# fondy

Fondy.eu Python SDK

## Install

```shell
pip install fondy
```

## Usage example

```python
from fondy import API
api = API(merchant_id, password, key)
api.invoice('20.00', 'UAH')
```
