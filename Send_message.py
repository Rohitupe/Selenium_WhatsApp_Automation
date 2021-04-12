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

# message user
send_message_to = ['BE PROJECT', 'Plan Squad', 'Aai', 'Karan Johar', 'Rohit Tupe']
file_path = "C:/Users/rohit/Desktop/samplePdf.pdf"


def send_message():
    message = "Hello, This is a Whatsapp Bot."
    driver.find_element_by_css_selector("div._1JAUF._2x4bz").send_keys(message)
    time.sleep(2)

    # send message
    driver.find_element_by_xpath("//div[@class='EBaI7']/button[@class='_1E0Oz']").click()


def send_file(file_path, user_name):
    if user_name == 'Aai':
        time.sleep(1)
        driver.find_element_by_xpath("//div[@title='Attach']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//input[@type='file' and @accept='*']").send_keys(file_path)
        time.sleep(2)
        driver.find_element_by_xpath("//div[@role='button']/span[@data-icon='send']").click()
    else:
        print("Not Special User")


def find_user(user_name):
    time.sleep(1)
    driver.find_element_by_xpath("//label[@class='RPX_m']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div[@class='_2_1wd copyable-text selectable-text']").clear()
    driver.find_element_by_xpath("//div[@class='_2_1wd copyable-text selectable-text']").send_keys(user_name)

    try:
        time.sleep(1)
        driver.find_element_by_xpath(f"//span[@title='{user_name}']").click()
        time.sleep(1)
        send_message()
        time.sleep(2)
        send_file(file_path, user_name)

    except Exception as e:
        print(f"User with name {user_name} Not Found!")


for user_name in send_message_to:
    try:
        time.sleep(1)
        driver.find_element_by_xpath(f"//span[@title='{user_name}']").click()
        time.sleep(1)
        send_message()
        time.sleep(3)
        send_file(file_path, user_name)

    except NoSuchElementException as se:
        print(f"Searching User {user_name}")
        find_user(user_name)

time.sleep(3)
driver.close()
driver.quit()
