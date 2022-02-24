#!/usr/bin/python3

from locale import currency
from bs4 import BeautifulSoup as bs
import requests, re

session = requests.Session()
user_agent = {'User-Agent':'LG8700/1.0 UP.Browser/6.2.3.9 (GUI) MMP/2.0'}



genshin_data = '''CNY	¥30[19]	1 : 0.1574	4.72	635.59
MYR	RM19.90[6]	1 : 0.2395	4.77	629.48
VND	109,000đ[13]	1 : 0.000044	4.80	624.92
PHP	₱249[12]	1 : 0.01959	4.88	615.07
HKD	HK$38[17]	1 : 0.1284	4.88	614.76
USD	$4.99[2]	1 : 1	4.99	601.20
BRL	R$27.90[11]	1 : 0.1809	5.05	594.48
SGD	S$6.98[7]	1 : 0.7443	5.19	577.49
THB	฿179[9]	1 : 0.03016	5.40	555.76
IDR	Rp79,000[8]	1 : 0.00007	5.52	543.05
CAD	$6.99[5]	1 : 0.801	5.60	535.82
EUR	€4.99[4]	1 : 1.148	5.73	523.84
AUD	$7.99[10]	1 : 0.7277	5.81	515.98
RUB	449₽[15]	1 : 0.01317	5.91	507.40
INR	₹449[16]	1 : 0.01349	6.06	495.30
PLN	23,99zł[14]	1 : 0.2529	6.07	494.52
GBP	£4.49[3]	1 : 1.371	6.15	487.49
TRY	₺84,99[18]	1 : 0.07376	6.27	478.52'''

table = genshin_data.split('\n')
for row in table:
    row = row.split('\t')
    currency = row[0]
    price = row[1]



index = bs(session.get('https://www.google.com/search?newwindow=1&oq=&aqs=&q=myr+exchange',headers=user_agent).text, 'html.parser')
exchange = index.html.body.contents[2].contents[0].div.div.table.tbody.tr.td.div.div.span.span.text
exchange = float(exchange.replace(' Российский рубль','').replace(',','.'))


print("Content-Type: text/html\n")
print('HELLO WORLD')