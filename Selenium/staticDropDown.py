from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get('https://the-internet.herokuapp.com/dropdown')
select = Select(driver.find_element_by_id('dropdown'))
select.select_by_visible_text('Option 2')