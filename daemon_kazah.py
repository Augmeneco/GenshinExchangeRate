#!/usr/bin/python3

from bs4 import BeautifulSoup as bs
import requests, time, json, datetime, traceback

def log(text):
    print(datetime.datetime.today().strftime("%H:%M:%S")+' | '+text)

while True:
    try:
        session = requests.Session()
        session.headers.update({'User-Agent':'LG8700/1.0 UP.Browser/6.2.3.9 (GUI) MMP/2.0'})
        config = json.loads(open('data/config_kazah.json','r').read())

        exchange_nosort = {}
        exchange = {}

        for currency in config['currency']:
            cost = config['currency'][currency][0]

            index = bs(session.get('https://www.google.com/search?newwindow=1&oq=&aqs=&q='+currency+'+курс к тенге').text, 'html.parser')
            data = index.html.body.contents[2].contents[0].div.div.table.tbody.tr.td.div.div.span.span.text
            data = float(data.replace(' Казахстанский тенге','').replace(',','.'))

            exchange_nosort[currency] = round(data*cost,2)
            
            if exchange_nosort[currency] > config['exchange'][currency]:
                config["currency"][currency][3] = '<span style="color: red;">▲</span>'
            if exchange_nosort[currency] < config['exchange'][currency]:
                config["currency"][currency][3] = '<span style="color: #17FF00;">▼</span>'
            #if exchange_nosort[currency] == config['exchange'][currency]:
            #    config["currency"][currency][3] = ''

        for k in sorted(exchange_nosort, key=exchange_nosort.get):
            exchange[k] = exchange_nosort[k]

        config['exchange'] = exchange
        config['last_check'] = time.time()

        open('data/config_kazah.json','w').write(json.dumps(config, indent=4))

        log('Complete')

    except Exception as error:
        log('Fail')
        print(traceback.format_exc())
        pass
    time.sleep(60*10)
