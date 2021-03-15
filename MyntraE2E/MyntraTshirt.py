import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe',
                          options=chrome_options)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://www.myntra.com/")

actions = ActionChains(driver)
actions.move_to_element(driver.find_element_by_link_text("Men"))
driver.find_element_by_link_text("T-Shirts").click()

brand_list = driver.find_elements_by_xpath("//ul[@class='brand-list']/li/label")

for brand in brand_list:
    if 'Puma' in brand.text:
        brand.find_element_by_xpath(".//div").click()
        break

time.sleep(2)
price_list = driver.find_elements_by_xpath("//ul[@class='price-list']/li/label/input")

for price in price_list:
    if price.get_attribute("value") == '2871.0 TO 5248.0':
        price.find_element_by_xpath(".//parent::label/div").click()
        break

time.sleep(2)
product_list = driver.find_elements_by_xpath("//div[@class='product-productMetaInfo']")
print(len(product_list))
for product in product_list:
    product_name = product.find_element_by_xpath(".//h4[@class='product-product']")
    print(product_name.text)

