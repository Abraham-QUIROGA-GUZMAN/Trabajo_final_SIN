
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/59.0.3071.115 Safari/537.36")

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=opts)

url = 'https://www.google.com/recaptcha/api2/demo'
driver.get(url)

try:

  driver.switch_to.frame(driver.find_element_by_xpath('//iframe'))
  captcha = driver.find_element_by_xpath('//div[@class="recaptcha-checkbox-border"]')
  captcha.click()

  input()

  
  driver.switch_to.default_content()

  submit_button = driver.find_element_by_xpath('//input[@id="recaptcha-demo-submit"]')
  submit_button.click()

except Exception as e:
  print (e)


print ("Bienvenido Abraham ya estas dentro...")

almacenamiento = driver.find_element_by_class_name('recaptcha-success')
print (almacenamiento.text)