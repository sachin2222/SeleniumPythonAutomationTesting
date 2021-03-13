from selenium import webdriver

from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe',
                          options=chrome_options)


driver.get("https://the-internet.herokuapp.com/forgot_password")
# actions = ActionChains(driver)
# ele1 = driver.find_element_by_xpath("//div[@class='example']/div[1]")
# actions.move_to_element(ele1).perform()

driver.execute_script("document.getElementById('email').value='Hello'")
e = driver.find_element_by_id("form_submit")
driver.execute_script("arguments[0].click();", e)
