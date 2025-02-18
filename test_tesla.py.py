import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://finance.yahoo.com/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(3)

#title verification
assert driver.title == "Yahoo Finance - Stock Market Live, Quotes, Business & Finance News"

#search for tesla
search_bar = driver.find_element(By.XPATH,'//input[@id="ybar-sbq"]')
search_bar.send_keys("TSLA")
time.sleep(3)

#verify auto suggestion
suggestion_text = driver.find_element(By.XPATH,"(//div[contains(text(),'TSLA')]/following-sibling::div[contains(text(),'Tesla, Inc.')])[1]").text
assert suggestion_text == "Tesla, Inc."

#click on first entry
first_tsla_suggestion = driver.find_element(By.XPATH,'//ul[@class="modules-module_list__hi5kT"]/li[@data-id="result-quotes-0"]')
first_tsla_suggestion.click()
time.sleep(5)

#verify TSLA price greater than 200
TSLA_price = driver.find_element(By.XPATH,'//span[@data-testid="qsp-price"]').text
assert float(TSLA_price) > 200,  "Failed because TSLA price is less than 200$"
time.sleep(5)

#previous close
previous_close_value = driver.find_element(By.XPATH,"//span[contains(text(),'Previous Close')]/following-sibling::span/*[@class='yf-gn3zu3']")
print(previous_close_value.text)
time.sleep(5)

#volume
volume = driver.find_element(By.XPATH,"//span[contains(text(),'Volume')]/following-sibling::span/*[@class='yf-gn3zu3']")
print(volume.text)
time.sleep(5)


