# Handling Checkbox dynamically
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

# store all the checkboxes in one list
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
# iterate over the list of checkboxes to click on them to select
print("{} {} {}".format("there are ", len(checkboxes), " checkboxes on the screen"))  # print length of the checkboxes
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()  # click on each checkbox
        assert checkbox.is_enabled()  # check if its enabled to be clicked or not
        assert checkbox.is_displayed()  # check if its displayed or not
        assert checkbox.is_selected()  # check if its selected or not
time.sleep(1)
radioButtons = driver.find_elements(By.CSS_SELECTOR, "input[class='radioButton']")
radioButtons[2].click()  # click on the element which has index 2 in the list
assert radioButtons[2].is_selected()
time.sleep(1)
