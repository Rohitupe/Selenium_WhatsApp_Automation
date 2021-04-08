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
# driver = webdriver.Chrome(executable_path="driver/chromedriver.exe")
driver.implicitly_wait(10)
# driver.maximize_window()

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
allMessages = driver.find_elements_by_xpath("//div[@class='TbtXF']/div[@class='_1SjZ2']/div[@class='_15smv']/span/div[@class='_2TiQe']/span[@class='_38M1B']")

for message_popup in allMessages:
    time.sleep(2)
    try:
        # //div/div[@class='_3Dr46']/span/ancestor::div[@class='TbtXF']/div/div[@class='_3Dr46']
        if int(message_popup.text) >= 1:
            print("yes" + message_popup.text)
            # username = message_popup.find_element_by_xpath("div/div[@class='_3Dr46']/span")
            username = message_popup.find_element_by_xpath("ancestor::div[@class='TbtXF']")
            username.click()
            time.sleep(2)
            message = driver.find_element_by_xpath("//div[@class='_2A8P4']")
            time.sleep(1)
            message.send_keys("Hello, Thanks for replying me.")
            time.sleep(1)
            # send message
            driver.find_element_by_xpath("//div[@class='EBaI7']/button[@class='_1E0Oz']").click()
        else:
            print("No new message Found")

    except NoSuchElementException as e:
        print("Element Not Found: ", e)

