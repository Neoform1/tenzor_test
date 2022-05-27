from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)


driver.get('http://www.yandex.ru/')
sleep(5) # Let the user actually see something!

search_box = driver.find_element(by=By.NAME, value='text')

search_box.send_keys('Тензор')
sleep(5)

search_box.submit()
sleep(5) 

driver.quit()