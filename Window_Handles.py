import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

#Login URL
driver.get("https://demo.automationtesting.in/Windows.html")

#Maximize window
driver.maximize_window()

#Click on Button
driver.find_element(By.XPATH,'//*[@id="Tabbed"]/a/button').click()

#print parent window value/ ID
print(driver.current_window_handle)

#handle value of open window.
handel = driver.window_handles

#More than one window handle for

for h in handel:
    driver.switch_to.window(h)
    print(driver.title)

    #close window
    '''if driver.title=="Selenium":
        driver.close()'''
time.sleep(2)
driver.quit()

#Mouse Actions
#1. Click()
#2. Double click()
#3. Right click()
#4. Drag and Drop
#5. Mouse hover

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.execute_script("window.scrollBy(0,500)"," ")
act=ActionChains(driver)

#Double click action
'''double_click1= driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
time.sleep(2)
act.double_click(double_click1).perform()

#Right click Action
double_click2= driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
time.sleep(2)
act.context_click(double_click2).perform()'''

#Drag and Drop
source=driver.find_element(By.XPATH,'//*[@id="draggable"]')

target=driver.find_element(By.XPATH,'//*[@id="droppable"]')

time.sleep(2)
act.drag_and_drop(source,target).perform()

