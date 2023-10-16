import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

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
