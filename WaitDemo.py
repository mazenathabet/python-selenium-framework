# Sometimes selenium needs to wait few seconds for the elements to appear or to finish loading etc
# it is a bad practice to use time.sleep() aka Thread.sleep in java because it is a static wait
# that is why its always a good practice to use dynamic waits like implicit wait or explicit waits
# Implicit Wait -> global wait for the whole driver object applicable to each step the driver do
# Explicit wait
# pause the test for few seconds -> time.sleep # BAD PRACTICE and its python not a selenium
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

driver.implicitly_wait(5)  # wait until 5 secs if element is not displayed
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

searchBar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']")
searchBar.send_keys("ber")
time.sleep(3)
count = len(driver.find_elements(By.CSS_SELECTOR, "div[class='product']"))
assert count == 3  # assert the number of displayed products

addToCartButtons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
len(addToCartButtons)
time.sleep(3)
for button in addToCartButtons:
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

promoInfo = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
assert "Code applied ..!" in promoInfo
