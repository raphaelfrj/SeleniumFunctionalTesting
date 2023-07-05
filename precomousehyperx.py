
from selenium import webdriver
import time

driver = webdriver.Chrome()


# Site Access
driver.get("https://google.com.br")
driver.implicitly_wait(5)
driver.maximize_window()

# Digitando na busca
driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea').send_keys('HyperX Pulsefire Core RGB 6200 DPI - 4P4F8AA')
time.sleep(2)
driver.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
time.sleep(3)

print('Valor do mouse HyperX Pulsefire Core RGB 6200 DPI - 4P4F8AA nos principais sites')

# Pegando valores dos principais sites
valorkabum=driver.find_element('xpath', '//*[@id="rso"]/div[1]/div/div/div[4]/div/span[4]')
print("Valor na Kabum:",valorkabum.text)

valorterabytes=driver.find_element('xpath', '//*[@id="rso"]/div[2]/div/div/div[4]/div/span[4]')
print("Valor na Terabyteshop:",valorterabytes.text)

valoramazon=driver.find_element('xpath','//*[@id="rso"]/div[3]/div/div/div/div[5]/div/span[4]')
print("Valor na Amazon:", valoramazon.text)

valorpichau=driver.find_element('xpath', '//*[@id="rso"]/div[5]/div/div/div[4]/div/span[1]')
print("Valor na Pichau:", valorpichau.text)

valormercadolivre=driver.find_element('xpath', '//*[@id="rso"]/div[7]/div/div/div[3]/div/span[4]')
print("Valor no Mercado Livre:", valormercadolivre.text)


time.sleep(3)
