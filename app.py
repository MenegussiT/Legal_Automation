#Automação Sulamerica
###-----Importação da biblioteca que lê excel----###
import pandas as pd
##importação de tempo
import time 
###-----Importação da biblioteca que trabalha na web----###
from selenium  import webdriver#Biblioteca para mexer com o navegador
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By#Achar Elementos
from selenium.webdriver.common.keys import Keys#Digitar nos elementos
from selenium.common.exceptions import NoSuchElementException#Não acaha elemento
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Excel
arquivo = 'LAYOUT SAUDE_RODAR1.xlsx'#ALTERAR DE ACORDO COM O ROBÔ CORRESPONDENTE
df= pd.read_excel(arquivo)
print(df)
#CONFIGURAÇÃO DE NAVEGADOR
servico = Service(ChromeDriverManager(version='114.0.5735.90').install())
#webdriver
navegador = webdriver.Chrome(service=servico)
#Area de login
while True:
    try:
        navegador.get('https://process.paas.sulamerica.com.br/process/logout')
        login = navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys("USER")
        senha= navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys("PASSWORD")
        botao_entrar= navegador.find_element(By.XPATH, '//*[@id="btn_logar"]').click()
        time.sleep(15)
    except NoSuchElementException:
        time.sleep(3)
        login = navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys("USER")
        senha= navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys("PASSWORD")
        pass
    break

for i, row in df.iterrows():
    try:
        
        navegador.find_element(By.XPATH,'//*[@id="pastaJuridica"]').send_keys(row["CIV"])
        navegador.find_element(By.XPATH,'//*[@id="pastaJuridica"]').send_keys(Keys.ENTER)
        time.sleep(4)
        navegador.find_element(By.XPATH,'//*[@id="btn_andamento"]').click()
        time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="li_new_andamento"]/table/tbody/tr/td').click()
        time.sleep(4)
        navegador.find_element(By.XPATH, '//*[@id="id_fase"]').click()
        time.sleep(3)
        navegador.find_element(By.XPATH, '//*[@id="id_fase"]/option[117]').click()
        time.sleep(2)
        navegador.find_element(By.XPATH, '//*[@id="id_fase_processual_andamento"]').click()
        navegador.find_element(By.XPATH, '//*[@id="id_fase_processual_andamento"]/option[15]').click()
        navegador.find_element(By.XPATH, '//*[@id="dt_andamento"]').click()
        navegador.find_element(By.XPATH, '//*[@id="dt_andamento"]').send_keys("18072023") #Data$$$%$$$$$$$$$$$$$
        navegador.find_element(By.XPATH, '//*[@id="descricao"]').send_keys(row["ANDAMENTO"])
        navegador.find_element(By.XPATH, '//*[@id="btn_gravar_and"]').click()
    except NoSuchElementException:
        time.sleep(12)
        continue
    
try:
    navegador.find_element(By.XPATH, '//*[@id="boxModalTimeout"]')
    navegador.find_element(By.XPATH, '//*[@id="confirmSessao"]').click()
except NoSuchElementException:
    time.sleep(6)
    pass

if navegador.find_element(By.XPATH,'https://process.paas.sulamerica.com.br/process/logout'):
    login = navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys("USER")
    senha= navegador.find_element(By.XPATH, '//*[@id="senha"]').send_keys("PASSWORD")
    botao_entrar= navegador.find_element(By.XPATH, '//*[@id="btn_logar"]').click()
else:
    pass