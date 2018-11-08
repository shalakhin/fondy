# fondy

Fondy.eu Python SDK

## Install

```shell
pip install fondy
```

## Usage example

```python
from fondy import API
api = API(merchant_id, merchant_key, server_callback_url)
# generate Fondy payment url to checkout 200 UAH for "123456" order id
api.checkout('123456', 200 * 100)
```

## Supported API endpoints

|----------------|----------------------|
|Endpoint        |Explanation           |
|order_status    |Check order status    |
|p2pcredit       |Pay to credit card    |
|checkout        |Generate checkout URL |

## Requirements

- requests
