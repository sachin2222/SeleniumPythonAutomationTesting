from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

col1 = driver.find_elements_by_xpath("//div[@class='tableFixHead']/table/tbody/tr/td[1]")
print(len(col1))
for i in range(len(col1)):
    print(col1[i].text)
    if 'Alex' in col1[i].text:
        e = col1[i].find_element_by_xpath(".//following-sibling::td[3]")
        print(e.text)
        break



