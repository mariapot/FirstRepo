from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import time

driver = webdriver.Firefox()
driver.get("http://jobmight.com/session/emp/signin")

email_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input.send_keys("kate@gmail.com")

pass_input: object = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
pass_input.send_keys("Kate20@")

# login_btn = WebDriverWait(driver, 20).until(
# (EC.element_to_be_clickable((By.XPATH, '//div[@id="root"]'))))
# login_btn.click()
login_btn = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH,
                '//div[@id="content"]/div/div/div/div/div/div[2]/div[2]/form/div[3]/div/button'))))
login_btn.click()
