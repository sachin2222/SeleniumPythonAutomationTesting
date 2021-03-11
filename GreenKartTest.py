from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_css_selector('.search-keyword').send_keys('ber')
veggies = driver.find_elements_by_xpath("//div[@class='product']/h4")

wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '.product-action')))
cart_list = driver.find_elements_by_css_selector('.product-action')
print(len(veggies))
print(len(cart_list))

for cart in cart_list:
    cart.click()
