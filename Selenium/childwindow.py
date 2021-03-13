from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\sachin\chromeWebdriver89\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
# driver.find_element_by_link_text('Click Here').click()
#
# child = driver.window_handles[1]
# driver.switch_to.window(child)
# print(driver.title)
# print(driver.current_url)
# frame1 = driver.find_element_by_id("mce_0_ifr")
# driver.switch_to.frame(frame1)
# driver.find_element_by_css_selector("body[id='tinymce']").send_keys("Hi , I am inside Frame")