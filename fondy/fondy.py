import json
import hashlib
import requests


class FondyAPI(object):
    """Basic Fondy API Wrapper"""
    ENDPOINTS = {
        'order_status': 'https://api.fondy.eu/api/status/order_id',
        'p2pcredit': 'https://api.fondy.eu/api/p2pcredit/'
    }

    def __init__(self, merchant_id, password, key, *args, **kwargs):
        self.merchant_id = merchant_id
        self.password = password
        self.key = key

    def sign(self, data):
        """
        Create signature https://portal.fondy.eu/en/info/api/v1.0/3/#chapter-5
        Takes dict like below and adds "signature" into the "request":

        {
          "request":{
            "order_id":"test123456",
            "order_desc":"test order",
            "currency":"USD",
            "amount":"125",
            "signature":"f0ee6288b9295d3b808bcd8d720211c7201245e1", <-- that
            "merchant_id":"1396424"
          }
        }
        """
        assert 'request' in data.keys()
        keys = sorted(data['request'].keys())
        values = [self.key]
        values += [data['request'][key] for key in keys]
        raw = '|'.join(values)
        data['request']['signature'] = hashlib.sha1(raw.encode('utf-8')).hexdigest()

        return json.dumps(data)

    def order_status(self, order_id):
        """
        Check order status
        https://portal.fondy.eu/en/info/api/v1.0/5#chapter-5-4-json
        """
        assert type(order_id) is str
        data = {
           'request': {
                'order_id': order_id,
                'merchant_id': self.merchant_id,
            }
        }
        endpoint = self.ENDPOINTS['order_status']
        headers = {'Content-Type': 'application/json'}
        return requests.post(endpoint, data=self.sign(data), headers=headers)

    def p2pcredit(self, order_id):
        assert type(order_id) is str
        data = {
           'request': {
                'order_id': order_id,
                'merchant_id': self.merchant_id,
            }
        }
        endpoint = self.ENDPOINTS['p2pcredit']
        headers = {'Content-Type': 'application/json'}
        return requests.post(endpoint, data=self.sign(data), headers=headers)
