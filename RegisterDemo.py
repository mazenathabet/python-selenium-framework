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

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element_by_xpath("//a[normalize-space()='Register']) --> is deprecated
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
assert "Register" in driver.title
########################################
# fill registration data
fName = "mazen"
lName = "Ahmed"
email = "mazenathabet221@gmail.com"
password = "123456789"

gender = "male"
if "male" == gender:
    driver.find_element(By.ID, "gender-male").click()
elif "female" == gender:
    driver.find_element(By.ID, "gender-female").click()
else:
    print("gender not found")
fNameBox = driver.find_element(By.ID, "FirstName")
fNameBox.send_keys(fName)
driver.find_element(By.NAME, "LastName").send_keys(lName)
# select class provides the methods to handle the options in dropdown- can be used only if the tag name is "Select"
daySelect = Select(driver.find_element(By.NAME, "DateOfBirthDay"))
daySelect.select_by_visible_text("18")
monthSelect = Select(driver.find_element(By.NAME, "DateOfBirthMonth"))
monthSelect.select_by_index(12)  # index starts with 0
yearSelect = Select(driver.find_element(By.NAME, "DateOfBirthYear"))
yearSelect.select_by_value("1992")
############################################
driver.find_element(By.ID, "Email").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#Password").send_keys(password)
driver.find_element(By.NAME, "ConfirmPassword").send_keys(password)
driver.find_element(By.ID, "register-button").submit()

# registration successfully assertion
registeredLabel = driver.find_element(By.XPATH, "//div[@class='result']")
print(registeredLabel.text)  # Your registration completed
assert "Your registration completed" == registeredLabel.text
assert "completed" in registeredLabel.text
