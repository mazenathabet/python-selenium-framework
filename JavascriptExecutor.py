# Js DOM can access any elements on web page just like how selenium does
# selenium have a method to execute javascript code in it
# there are some instances to either access the element or identify an element in that time
# you can still access that element using java script to click or send keys

from selenium import webdriver
from selenium.webdriver.common.by import By
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
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

driver.find_element(By.NAME, "name").send_keys("hello")
print(driver.find_element(By.NAME, "name").text)
# will return blank text because selenium usually stores the element at the beginning of the page once its loaded
print(driver.find_element(By.NAME, "name").get_attribute("value"))  # you can get the value entered with this way
############################################
# driver.execute_script() is to execute java script actions - selenium here is giving its control to java script
# returning a value entered in the first element that has name = name
print(driver.execute_script('return document.getElementsByName("name")[0].value'))
# sometimes some pop up comes over an element and selenium will not be able to click it
# in this case we can use java script to click it and it will click on the element
# on the DOM instead of the frontend view
shopButton = driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)
# selenium does not support scrolling down but java script does
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

