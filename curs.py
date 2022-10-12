# -*- coding: utf-8 -*-
# !usr/bin/env python
import requests

r = requests.get('https://www.blockchain.com/ticker')
bitprice = (r.json()['RUB']['buy'])
bitpriceUSD = (r.json()['USD']['buy'])
