# Function for getting user from
def new_chat(user, driver, time):
    # Selecting the new chat search textbox
    new_chat = driver.find_element_by_xpath('//div[@class="ZP8RM"]')
    new_chat.click()

    # Enter the name of chat
    new_user = driver.find_element_by_xpath('//div[@class="_3u328 copyable-text selectable-text"]')
    new_user.send_keys(user)

    time.sleep(1)

    try:
        # Select for the title having user name
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        # Close the browser
        chrome_browser.close()
        print(e)
        sys.exit()