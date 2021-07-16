from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options


@given('I have open the login page')
def launchBrowser(context):
    option1 = Options()
    option1.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe", chrome_options=option1)
    context.driver.maximize_window()
    context.driver.get("https://www.axisbank.com")



@when('I click on login button')
def openLoginPage(context):
    login = context.driver.find_element_by_xpath("//div[@class='loginClk jsloginClk']")
    actions = ActionChains(context.driver)
    actions.move_to_element(login).perform()


@then('I should see register button')
def verifyButton(context):
    status=context.driver.find_element_by_xpath("//a[contains(text()[1],'Register')]").is_displayed()
    assert status is True


@then('close the browser')
def closeBrowser(context):
    context.driver.close()




