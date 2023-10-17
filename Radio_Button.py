import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_version=Options()
chrome_version.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_version)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,1000)"," ")
time.sleep(3)

driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span').click()
time.sleep(3)

# driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
Male= driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span')

if Male.is_selected():
    pass
else:
    Male.click()
    print("Male Radio button is selected")
time.sleep(3)


# Alert Button
driver.get("https://demo.automationtesting.in/Alerts.html")

# driver.find_element(By.XPATH,"//a [@aria-expanded='true']").click()
# driver.find_element(By.XPATH,"//button[@class='btn btn-danger']").click()
# time.sleep(3)
# atr = driver.switch_to.alert
# atr.accept()

driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(2)

# To Accept the POP_UP window
atr = driver.switch_to.alert
atr.accept()

# To Close the POP_UP window
#atr.dismiss()

handel = driver.window_handles

#More than one window handle for

for h in handel:
    driver.switch_to.window(h)
    print(driver.title)



