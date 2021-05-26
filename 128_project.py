from bs4 import BeautifulSoup
import requests
import pandas as pd
URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(URL)
#print(page)
soup = BeautifulSoup(page.text,'html.parser')
table = soup.find_all('table')
print(len(table))
temp_list = []
table_row = table[4].find_all('tr')
for tr in table_row:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)
print(temp_list)