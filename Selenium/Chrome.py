from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/login')
print(driver.current_url)
driver.get('https://google.com')
print(driver.title)
driver.back()
print(driver.title)
driver.quit()

