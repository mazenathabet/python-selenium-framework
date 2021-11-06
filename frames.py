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
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
# switch to a frame
driver.switch_to.frame("mce_0_ifr")  # frame ID , frame name , or index value
driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("HELLO FROM IFRAME")
driver.switch_to.default_content()  # to return back to the default content / frame
print(driver.find_element(By.CSS_SELECTOR, "div[class='example'] h3").text)  # parent frame element
