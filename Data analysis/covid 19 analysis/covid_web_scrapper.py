# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:30:49 2024

@author: Pavan
"""

from bs4 import BeautifulSoup
import pandas as pd 
import requests


url = "https://www.worldometers.info/coronavirus/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}

response = requests.get(url,headers=headers)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

prettify_page = soup.prettify()

CountryNames = soup.find_all("a",class_="mt_a")
TotalCasesodd = soup.find_all('tr', class_="odd")
TotalCaseseven = soup.find_all('tr', class_="even")

Country_names = []
Total_cases = []

for names in CountryNames:
    Country_names.append(names.text)

for cases in TotalCasesodd:
    print(cases.text)