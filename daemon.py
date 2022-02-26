#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests, time, json

session = requests.Session()
session.headers.update({'User-Agent':'LG8700/1.0 UP.Browser/6.2.3.9 (GUI) MMP/2.0'})
config = json.loads(open('config.json','r').read())

exchange_nosort = {}
exchange = {}

for currency in config['currency']:
    cost = config['currency'][currency][0]

    index = bs(session.get('https://www.google.com/search?newwindow=1&oq=&aqs=&q='+currency+'+exchange').text, 'html.parser')
    data = index.html.body.contents[2].contents[0].div.div.table.tbody.tr.td.div.div.span.span.text
    data = float(data.replace(' Российский рубль','').replace(',','.'))

    exchange_nosort[currency] = round(data*cost,2)

for k in sorted(exchange_nosort, key=exchange_nosort.get, reverse=True):
    exchange[k] = exchange_nosort[k]

config['exchange'] = exchange
config['last_check'] = time.time() 

open('config.json','w').write(json.dumps(config, indent=4))

#datetime.datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')