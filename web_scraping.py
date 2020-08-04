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
driver.implicitly_wait(20)
time.sleep(15)

a= driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]/div[2]/div[1]')

html = a.get_attribute("innerHTML") 
print(html)
b=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]/div[2]/div[1]')

html2 = b.get_attribute("innerHTML") 
print(html2)

