from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

browserType = "firefox"
if "chrome" in browserType:
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif "firefox" in browserType:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Click Here").click()  # the main/parent window
windows = driver.window_handles # will return all the windows ids as List of Str
childWindow = windows[1]
driver.switch_to.window(childWindow)
print(driver.find_element(By.TAG_NAME, "h3").text)  # the child window
assert "New Window" in driver.find_element(By.TAG_NAME, "h3").text
driver.close()
driver.switch_to.window(windows[0])
print(driver.find_element(By.TAG_NAME, "h3").text)
assert "Opening a new window" in driver.find_element(By.TAG_NAME, "h3").text


