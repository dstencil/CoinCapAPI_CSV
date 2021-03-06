from requests.api import head
import requests
import csv
from datetime import datetime
from datetime import date
import os.path 



url = 'http://api.coincap.io/v2/assets'

headers = {
	'Accept': 'application/json',
	'Content-Type': 'application/json'
}
responses = requests.request("GET", url,headers=headers, data= {})
myjson = responses.json()
ourdata = []
headers = ['SYMBOL', 'NAME', 'PRICE(USD)', 'TIME']
file_exists = os.path.exists(f'coincap{date.today()}.csv')

for x in myjson['data']:
    listing = [x['symbol'],x['name'],x['priceUsd'],datetime.now()]
    ourdata.append(listing)

with open(f'coincap{date.today()}.csv', 'a+',encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(headers)
    writer.writerows(ourdata)
    
print('done')
