# Sometimes selenium needs to wait few seconds for the elements to appear or to finish loading etc
# it is a bad practice to use time.sleep() aka Thread.sleep in java because it is a static wait
# that is why its always a good practice to use dynamic waits like implicit wait or explicit waits
# Implicit Wait -> global wait for the whole driver object applicable to each step the driver do
# Explicit wait -> target only specific element for a condition to be happened
# pause the test for few seconds -> time.sleep # BAD PRACTICE and its python not a selenium
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

searchBar = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search for Vegetables and Fruits']")
searchBar.send_keys("ber")
count = len(driver.find_elements(By.CSS_SELECTOR, "div[class='product']"))
assert count == 3  # assert the number of displayed products
time.sleep(2)
addToCartButtons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")

len(addToCartButtons)
for button in addToCartButtons:
    button.click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'PROCEED TO CHECKOUT')]").click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter promo code']")))
originalAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
driver.find_element(By.XPATH, "//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))
promoInfo = driver.find_element(By.XPATH, "//span[@class='promoInfo']").text
discountAmount = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert float(discountAmount) < int(originalAmount)  # int(object) is to convert the string to int
assert "Code applied" in promoInfo
driver.delete_all_cookies()
