from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element_by_id('autosuggest').send_keys('am')
countries = driver.find_elements_by_xpath("//li[@class='ui-menu-item']/a")
print(len(countries))

for country in countries:
    if country.text == 'Gambia':
        country.click()
        break

driver.find_element_by_id('ctl00_mainContent_ddl_originStation1_CTXT').click()
source_List = driver.find_elements_by_css_selector("[id='dropdownGroup1'] [class='dropdownDiv'] li")

for source in source_List:
    if 'DEL' in source.text:

        source.click()
        break

driver.find_element_by_id('ctl00_mainContent_ddl_destinationStation1_CTXT').click()
destination_List = driver.find_elements_by_css_selector("[id='dropdownGroup1'] [class='dropdownDiv'] li")


for dest in destination_List:
    if 'BOM' in dest.text:
        dest.click()
        break
















