# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 18:30:49 2024

@author: Pavan
"""

from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests


url = "https://www.worldometers.info/coronavirus/"

web_page = requests.get(url)
soup = bs(web_page.text, "html.parser")
pret = soup.prettify()