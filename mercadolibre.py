from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)

driver.get('https://listado.mercadolibre.com.ec/repuestos-autos-camionetas-bujias')



MAXIMO = 10
INICIAL = 1


try:
  disclaimer = driver.find_element(By.XPATH, '//button[@id="cookieDisclaimerButton"]')
  disclaimer.click()
except Exception as e:
  print (e) 
  None


while MAXIMO > INICIAL:

  links_productos = driver.find_elements(By.XPATH, '//a[@class="ui-search-item__group__element ui-search-link"]')
  links_de_la_pagina = []
  for a_link in links_productos:
    links_de_la_pagina.append(a_link.get_attribute("href"))
 

  for link in links_de_la_pagina:

    try:
     
      driver.get(link)

     
      titulo = driver.find_element(By.XPATH, '//h1').text
      precio = driver.find_element(By.XPATH, '//span[contains(@class,"price-tag ui-pdp-price__part")]').text
      print (titulo)
      print (precio.replace('\n', '').replace('\t', ''))

      
      driver.back()
    except Exception as e:
      print (e)
      
      driver.back()

  
  try:
    
    puedo_seguir_horizontal = driver.find_element(By.XPATH, '//span[text()="Siguiente"]')
    puedo_seguir_horizontal.click()
  except: 

    break

  INICIAL += 1
