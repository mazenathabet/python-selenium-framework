import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserType = "chrome"
if "chrome" in browserType:
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif "firefox" in browserType:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# prompt alerts
Name = "Mazen Ahmed"
driver.find_element(By.ID, "name").send_keys(Name)
confirmAlertButton = driver.find_element(By.ID, "alertbtn")
confirmAlertButton.click()
alert = driver.switch_to.alert
alertActualText = alert.text
assert Name in alertActualText
print(alert.text)
alert.accept()

########################
# Confirm alert
confirmAlertButton = driver.find_element(By.ID, "confirmbtn")
confirmAlertButton.click()
confirmAlert = driver.switch_to.alert
time.sleep(1)
print(confirmAlert.text)
confirmAlert.accept()
time.sleep(1)
confirmAlertButton.click()
confirmAlert2 = driver.switch_to.alert
time.sleep(1)
confirmAlert2.dismiss()
