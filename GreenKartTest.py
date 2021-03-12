import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_css_selector('.search-keyword').send_keys('ber')
time.sleep(2)
veggie = driver.find_element_by_xpath("//div[@class='product']")
productName = veggie.find_elements_by_xpath("//h4")
addToCartButton = veggie.find_elements_by_xpath("//div[3]/button")

# for cart in addToCartButton:
#     cart.click()


for product in productName:
    if 'Raspberry' in product.text:
        print(product.text)
