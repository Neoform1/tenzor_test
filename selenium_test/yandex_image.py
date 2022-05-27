import time
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)



driver.get('https://www.yandex.ru/')

image_box = driver.find_element(by=By.CLASS_NAME, value="services-new__icon_images")
image_box.click()

base_window = driver.window_handles[0]
second_window = driver.window_handles[1]
driver.switch_to.window(second_window)

image_box = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a")
image_box.click()
time.sleep(2)

image_box = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img")
image_box.click()
time.sleep(2)

image_box = driver.find_element(by=By.XPATH, value="/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]/i")
image_box.click()
time.sleep(2)

image_box = driver.find_element(by=By.XPATH, value="/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[1]/i")
image_box.click()
time.sleep(5)

driver.quit()