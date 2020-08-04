import pandas as pd
import numpy as np
import matplotlib as plt
import os
import io
import requests
from io import StringIO
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

	
driver = webdriver.Firefox()
driver.get('https://covid.saude.gov.br/')
time.sleep(15)

a= driver.find_element_by_class_name('lb-total')

html = a.get_attribute("innerHTML") 
print(html)
b=driver.find_element_by_class_name('card-total tp-geral')

html2 = b.get_attribute("innerHTML") 
print(html2)
data=driver.find_element_by_class_name("lb-grey")
data_html=data.get_attribute("innerHTML") 
print(data_html)
casos_obitos= driver.find_element_by_class_name('lb-total')
