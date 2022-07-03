#!/usr/bin/python3

import json, datetime, os, sqlite3, sys

#history_db = sqlite3.connect('data/history.db')

config = json.loads(open('data/config.json','r').read())

GET = {}

if os.environ['QUERY_STRING'] != '':
    QUERY_STRING = os.environ['QUERY_STRING'].split('&')
    for arg in QUERY_STRING:
        arg = arg.split('=')
        GET[arg[0]] = arg[1]

print("Content-type: text/html; charset=utf-8\n")

html = '''
<html>
   <head>
      <title>GI Exchange Rate</title>
      <link rel="shortcut icon" href="data/icon.png" type="image/png">
      <meta http-equiv="content-type" content="text/html; charset=UTF-8">
      <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8">
      <meta http-equiv="content-style-type" content="text/css">
      <meta http-equiv="expires" content="0">
      <link rel="stylesheet" type="text/css" href="data/main.css">
   </head>
   <body>
      <a href="./">
         <div class="title">
            GI Exchange Rate
            <div class="news_date">Последнее обновление: {last_check}</div>
         </div>
      </a>
      <table cellspacing="0" id="maket">
      <tr>
         <td id="leftcol">
            <div style="font-size: 140%;">
               <a href="/index.py" class="btm"> Главная </a>
               <a href="/index.py?menu=contacts" class="btm"> Контакты </a>
               <a href="https://rentry.org/genshpay" class="btm"> Гайд по оплате с VPN </a>
               <a href="/index.py?menu=sourcecode" class="btm"> Исходный код </a>
               <a href="/index.py?menu=kazah" class="btm"> Версия для Казахов </a>
               <img src="data/zhongli.png"/ width="250px">
            </div>
         </td>
'''

html = html.format(
    last_check=datetime.datetime.fromtimestamp(config['last_check']).strftime('%H:%M:%S | %Y.%m.%d')
)

if 'menu' not in GET:
    html += '''<td id="rightcol">
                <div class="menu" style="margin: 0;">
                <div style="text-align: left; margin-left: 10px">
                    <b>Стоимость Благословения полой луны в Рублях: 449 ₽</b>
                </div>

                <!-- валюты -->
                {prices}

                </div>
            </td>
    </body>
    </html>'''
    prices = ''
    for price in config['exchange'].keys():
        prices += '''
            <div class="news_div">
                <div stype="font-size: 200%">{0} ₽ в {1} {2}</div>
            </div><br>
        '''.format(config['exchange'][price], config['currency'][price][2], config['currency'][price][3])

    html = html.format(
        prices=prices
    )
else:
    if GET['menu'] == 'contacts':
        html += '''<td id="rightcol">
                    <div class="menu" style="margin: 0;">
                    <div style="text-align: left; margin-left: 10px">
                        <b>Контакты:</b>
                    </div>

                    <div class="news_div">
                        <a href="https://vk.com/reikoshiki">ВКонтакте</a>
                    </div><br>

                    <div class="news_div">
                        <a href="https://t.me/cha14ka">Telegram</a>
                    </div><br>

                    </div>
                </td>
        </body>
        </html>'''

    if GET['menu'] == 'sourcecode':
        html += '''<td id="rightcol">
                    <div class="menu" style="margin: 0;">
                    <div style="text-align: left; margin-left: 10px">
                        <b>Исходный код движка сайта и демона:</b>
                    </div>

                    <div class="news_div">
                        <a href="https://github.com/Augmeneco/GenshinExchangeRate">GitHub</a>
                    </div><br>

                    </div>
                </td>
        </body>
        </html>'''
    
    if GET['menu'] == 'debug':
        html += '''<td id="rightcol">
                    <div class="menu" style="margin: 0;">
                    <div style="text-align: left; margin-left: 10px">
                        <b>GET:</b>
                    </div>
                    <div class="news_div">
                        {}
                    </div><br>
                    
                    <div style="text-align: left; margin-left: 10px">
                        <b>POST:</b>
                    </div>
                    <div class="news_div">
                        {}
                    </div><br>

                    </div>
                </td>
        </body>
        </html>'''
    if GET['menu'] == 'kazah':
        config = json.loads(open('data/config_kazah.json','r').read())
        html += '''<td id="rightcol">
                    <div class="menu" style="margin: 0;">
                    <div style="text-align: left; margin-left: 10px">
                        <b>Стоимость Благословения полой луны в Тенге: 2490 KZT</b>
                    </div>

                    <!-- валюты -->
                    {prices}

                    </div>
                </td>
        </body>
        </html>'''
        prices = ''
        for price in config['exchange'].keys():

            prices += '''
                <div class="news_div">
                    <div stype="font-size: 200%">{0} KZT в {1} {2}</div>
                </div><br>
            '''.format(config['exchange'][price], config['currency'][price][2], config['currency'][price][3])

        html = html.format(
            prices=prices
        )

print(html.format(os.environ, sys.stdin.read()))
