import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_version=Options()
chrome_version.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_version)

driver.get("http://omayo.blogspot.com/")
driver.maximize_window()
time.sleep(3)
driver.execute_script("window.scrollBy(0,500)"," ")

drop1=Select(driver.find_element(By.ID,'drop1'))
#1.select by visible text
drop1.select_by_visible_text("doc 3")
# 2.select by value
time.sleep(3)
drop1.select_by_value("mno")
# 3.select by Index
time.sleep(3)
drop1.select_by_index(1)

# count number of options
print(len(drop1.options))
# capture all the options
all1=drop1.options
for opt1 in all1:
    print(opt1)

# Locator Id
driver.find_element(By.ID,'ta1').send_keys("This is sample text in the page")
time.sleep(3)
driver.find_element(By.XPATH,"//select[@id='drop1']").click()
time.sleep(3)

