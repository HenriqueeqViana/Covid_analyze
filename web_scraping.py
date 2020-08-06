#Bibliotecas utilizadas e que serão utilizadas no desenvolvimento
import pandas as pd
import numpy as np
import matplotlib as plt
import os
import io
import re
import requests
from io import StringIO
import requests
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
#Roda o mozila em background.
options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options, executable_path="C:\\Users\\henri\\AppData\\Local\\Programs\\Python\\Python38-32\\geckodriver.exe")
#Inicia o bot no FireFox	
driver.get('https://covid.saude.gov.br/')
driver.implicitly_wait(20)
#retira o primeira string com o valor dos casos acumulados da pagina html
a= driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[2]/div[2]/div[1]').text
#Trata  string
def transf_numerico(str):
    regex_syntax = r"\D" #define variavel que vai tratar a string
    num_str = re.sub(regex_syntax, "", str) #retira parte não numerica
    numerico = float(num_str) #transforma em float
    return numerico

acumulados=transf_numerico(a)
#Retira a segunda string com o valor dos dados de mortes da pagina web
b=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[3]/div[2]/div[1]').text

mortos_acumulados=transf_numerico(b)

#Recuperados
c=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/painel-geral-component/div/card-totalizadores-component/div/div[1]/div[1]').text
recuperados=transf_numerico(c)
# Data dos dados atualizados
d=driver.find_element_by_xpath('/html/body/app-root/ion-app/ion-router-outlet/app-home/ion-content/div[1]/div[1]/div[3]/span').text
print(d)