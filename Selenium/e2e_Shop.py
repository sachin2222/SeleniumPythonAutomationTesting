from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe',
                          options=chrome_options)
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
phone_list = driver.find_elements_by_xpath("//div[@class='card-body']")
for phone in phone_list:
    phoneName = phone.find_element_by_xpath(".//h4/a").text
    if phoneName == 'Blackberry':
        phone.find_element_by_xpath(".//following-sibling::div/button").click()

driver.find_element_by_css_selector(".nav-link.btn.btn-primary").click()
driver.find_element_by_css_selector(".btn.btn-success").click()
driver.find_element_by_id("country").send_keys("In")
countryList = driver.find_elements_by_xpath("//div[@class='suggestions']/ul")


for country in countryList:
    if country.text == 'India':
        country.click()
        break

driver.find_element_by_css_selector("label[for='checkbox2']").click()

driver.find_element_by_css_selector(".btn.btn-success.btn-lg").click()
print(driver.find_element_by_css_selector(".alert.alert-success.alert-dismissible").text)
