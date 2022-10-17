#!/usr/bin/env python
#Shows the currency conversion from U$D to ArgDolarBlue
#Needs jq installed ( sudo apt-get install jq)
import requests

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'

json = requests.get(URL).json()

print()
print(' 💵 | compra | venta')
print('----|--------|-------')

for index, emoji in enumerate(('🟢', '🔵')):
    compra = json[index]['casa']['compra'][:-1]
    venta = json[index]['casa']['venta'][:-1]

    print(f" {emoji} |  {compra} | {venta}")

print()
