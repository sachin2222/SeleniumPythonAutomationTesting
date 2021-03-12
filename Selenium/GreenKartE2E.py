from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.implicitly_wait(5)
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
wait = WebDriverWait(driver, 10)

products = driver.find_elements_by_css_selector(".product-name")
veggie_list = ['Beans', 'Beetroot', 'Potato', 'Mango']


def fun(str):
    i = 0
    for i in range(len(products)):
        print(products[i].text)
        if str in products[i].text:
            driver.find_elements_by_xpath("//div[@class='product-action']/button")[i].click()
        i = i + 1


for k in range(len(veggie_list)):
    fun(veggie_list[k])

driver.find_element_by_xpath("//a[@class='cart-icon']").click()
driver.find_element_by_xpath("//div[@class='cart-preview active']/div[2]/button").click()
driver.find_element_by_css_selector(".promoCode").send_keys("12345")
driver.find_element_by_css_selector(".promoBtn").click()

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo')))
print(driver.find_element_by_css_selector(".promoInfo").text)

shopping_list = driver.find_elements_by_css_selector(".product-name")

required_list = []
for shop in shopping_list:
    vegetable = shop.text
    required_list.append(vegetable.split("-")[0].strip())

print(required_list)

assert required_list == veggie_list
