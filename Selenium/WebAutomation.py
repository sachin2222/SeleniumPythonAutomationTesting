from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/login')
driver.find_element_by_id('username').send_keys('Sachin')
driver.find_element_by_id('password').send_keys('Password')
driver.find_element_by_xpath("//button[@type='submit']").click()
message = driver.find_element_by_css_selector('div.flash.error').text

assert 'invalid' in message
