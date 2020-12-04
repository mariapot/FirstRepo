from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://jobmight.com/session/emp/signup")

email_input_field = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("mp@gmail.com")

company_name = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "companyName"))))
company_name.send_keys("SNM")

password = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("Maaria18@)")

your_full_name = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "yourName"))))
your_full_name.send_keys("Mike")

next_field = WebDriverWait(driver, 20).until(
    (EC.element_to_be_clickable((By.XPATH, '//div[@id="content"]/div/div/div/div/div/div[2]/div[3]/div[2]/button[2]'))))
next_field.click()

company_website = WebDriverWait(driver, 20).until((EC.visibility_of_element_located(
    (By.XPATH, '//div[@id="content"]/div/div/div/div/div/div[2]/div[3]/div/form/div/div/div/input'))))
company_website.send_keys("mmm@gmail.com")

zip_code = WebDriverWait(driver, 20).until((EC.visibility_of_element_located(
    (By.XPATH, '//div[@id="content"]/div/div/div/div/div/div[2]/div[3]/div/form/div[2]/div/div/input'))))
zip_code.send_keys("15220")

your_title_input = WebDriverWait(driver, 20).until(
    (EC.element_to_be_clickable((By.XPATH, "//div[@id='demo-simple-select']"))))
your_title_input.click()

your_title_field = WebDriverWait(driver, 20).until(
    (EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'HR')]"))))
your_title_field.click()
your_title_field.click()

back_but = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, '//button[@type="button"]'))))
back_but.click()
driver.quit()

driver.quit()
