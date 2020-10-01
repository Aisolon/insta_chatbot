from time import sleep

from selenium import webdriver


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        print("Logging in...")

    def go_to_directs(self):
        directs_button = self.browser.find_element_by_css_selector("[aria-label='Direct']").click()
        print("Going to direct messages...")
        return DirectsPage(self.browser)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
        try:
            self.browser.find_element_by_xpath("//a[text()='Log in']").click()
            sleep(2)
            return LoginPage(self.browser)
        except:
            return LoginPage(self.browser)
        finally:
            return LoginPage(self.browser)

class DirectsPage:
    def __init__(self, browser):
        self.browser = browser

    def find_messages(self, name):
        self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        # self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[5]/a").click()
        message_tab = self.browser.find_element_by_partial_link_text(name)
        print("Returning message tab...")
        return message_tab
        
    def send_message(self, message_tab, message):
        message_tab.click()
        message_input = self.browser.find_element_by_css_selector(".ItkAi > textarea:nth-child(1)")
        sleep(2)
        print(f"Sending message: {message}")
        message_input.send_keys(message)
        sleep(2)
        message_input.send_keys("\n")
        sleep(2)
        print("Sent message!")

def test_login_page(browser, username, password):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(username, password)

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

def navigate_to_direct_messages(browser, username, password):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(username, password)

    directs_page = login_page.go_to_directs()

    return directs_page

def message_someone(browser, name, message):
    directs_page = navigate_to_direct_messages(browser, username, password)
    specific_chat = directs_page.find_messages(name)
    directs_page.send_message(specific_chat, message)

browser = webdriver.Firefox()
browser.implicitly_wait(3)


username = "bernd.martin2305"
password = "HCDj1d5$3€"

recipient = "heinz"

message = "Hello World"

message_someone(browser, recipient, message)

browser.close()

