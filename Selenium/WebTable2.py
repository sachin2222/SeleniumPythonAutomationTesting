from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.window_handles()

col4 = driver.find_elements_by_xpath("//div[@class='tableFixHead']/table/tbody/tr/td[4]")
print(len(col4))

for i in range(len(col4)):
    print(col4[i].text)
    e = col4[i].find_element_by_xpath(".//preceding-sibling::td[3]")
    print(e.text)
