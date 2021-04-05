from selenium import webdriver
import time
# explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# exceptions
from selenium.common.exceptions import NoSuchElementException

# chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--user-data-dir=C:/Users/rohit/AppData/Local/Google/Chrome/User Data')
chrome_options.add_argument('--profile-directory=Default')

driver = webdriver.Chrome(executable_path="driver/chromedriver.exe", options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://web.whatsapp.com/")

# check whether user is already sign in or not
try:
    check = driver.find_element_by_xpath("//input[@name='rememberMe']").is_selected()
    if not check:
        driver.find_element_by_xpath("//input[@name='rememberMe']").click()
except:
    print("keep me Signed in is check - user already sign in")

# if not sign in wait for user to scan QR Code
try:
    wait = WebDriverWait(driver, 20)
    element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='_1xaVK']")))
except:
    driver.close()
    driver.quit()

# get all users who had sent message to me
allUsers = driver.find_elements_by_xpath("//div[@class='TbtXF']")

for user in allUsers:
    user.find_element_by_xpath("/")