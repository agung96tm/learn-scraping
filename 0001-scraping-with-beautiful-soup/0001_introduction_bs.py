from bs4 import BeautifulSoup
import requests


base_url = "https://subslikescript.com"
response = requests.get(f'{base_url}/movie/The_Wedding_in_the_Hamptons-21816848')
bs = BeautifulSoup(response.text, 'lxml')

box = bs.find('article', {'class': 'main-article'})
title = box.find('h1')
description = box.find('p', {'class': 'plot'})


print('============================================================')
print(title.get_text())
print('============================================================')
print("description", description.get_text())