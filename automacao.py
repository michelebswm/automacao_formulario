import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

tabela = pd.read_excel('challenge.xlsx')
print(tabela)
# Criando o navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.rpachallenge.com/')
time.sleep(2)  # Esperar carregar

# Botão Começar
navegador.find_element(By.XPATH, '//button[@class="waves-effect col s12 m12 l12 btn-large uiColorButton"]')


for i, coluna in tabela.iterrows():
    valor = tabela.iloc[i, ]

    # Email - Busca o Input @ng-reflect-name='labelEmail'
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelEmail']").send_keys(valor['Email'])

    # Company Name = ng-reflect-name="labelCompanyName"
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelCompanyName']").send_keys(valor['Company Name'])

    # lastName = ng-reflect-name="labelLastName"
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelLastName']").send_keys(valor['Last Name '])

    # roleCompany = ng-reflect-name="labelRole"
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelRole']").send_keys(valor['Role in Company'])

    # Phone = ng-reflect-name="labelPhone"
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelPhone']").send_keys(str(valor['Phone Number']))

    # firsName = ng-reflect-name="labelFirstName"
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']").send_keys(valor['First Name'])

    # adress = ng-reflect-name="labelAddress"
    navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelAddress']").send_keys(valor['Address'])

    # submit =
    navegador.find_element(By.XPATH, "//input[@class='btn uiColorButton']").click()
    time.sleep(2)
