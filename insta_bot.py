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
        sleep(5)

    def go_to_directs(self):
        directs_button = self.browser.find_element_by_css_selector("[aria-label='Direct']").click()
        sleep(2)
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
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[5]/a").click()
        message_input = self.browser.find_element_by_css_selector(".ItkAi > textarea:nth-child(1)")
        message_input.send_keys("This message was sent by the bot")
        message_input.send_keys("\n")

def test_login_page(browser, username, password):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(username, password)

    errors = browser.find_elements_by_css_selector('#error_message')
    assert len(errors) == 0

def go_to_directs(browser, username, password):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(username, password)

    directs_page = login_page.go_to_directs()

    return directs_page

def message_someone(browser, name):
    directs_page = go_to_directs(browser, username, password)
    specific_chat = directs_page.find_messages(name)

browser = webdriver.Firefox()
browser.implicitly_wait(5)


username = "bernd.martin2305"
password = "HCDj1d5$3€"

zottel = "zottelcorn"

message_someone(browser, zottel)

browser.close()

