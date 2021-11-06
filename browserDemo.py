from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# browser exposes an executable file
# Through selenium test we need to invoke the executable file which will then invoke actual browser
# driver = webdriver.Chrome(executable_path="D:\\Study materials and projects\\chromedriver_win32\\chromedriver.exe")
browserType = "chrome"

if "chrome" in browserType:
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif "firefox" in browserType:
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
assert driver.title == "nopCommerce demo store"  # assert equals
assert "demo" in driver.title  # is driver.title contains " demo " ? #true or false
driver.get("https://the-internet.herokuapp.com/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.quit()
# driver.close()
