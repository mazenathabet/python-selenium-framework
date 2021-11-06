from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

dropDownElement = driver.find_element(By.ID, "dropdown")
dropdown = Select(dropDownElement)
# dropdown.select_by_index() # select by index starts from 0
# dropdown.select_by_value() # select by value
# dropdown.select_by_visible_text() # select by visible text
# dropdown.is_multiple # bool to check if this dropdown is multiple or not
# dropdown.deselect_all() # to deselect all
# dropdown.deselect_by_index()
# dropdown.deselect_by_value()
# dropdown.deselect_by_visible_text()
# print(dropdown.first_selected_option)  # get first selected option
# print(dropdown.options)
