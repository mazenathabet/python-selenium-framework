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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
#############################################################
# How to deal with suggestive dropdown when suggestions appear when enter a value in the text
#############################################################
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries))  # to show the length of a list
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element(By.ID, "autosuggest").text)
# it will return blank because the selenium loads all the elements only when the page reloads
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
# so here we get the value attribute which will be updated with the selected value and print it
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"
time.sleep(2)
