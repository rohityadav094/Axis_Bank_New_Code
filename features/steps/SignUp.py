from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options



@given('open the login page')
def launchBrowser(context):
    option1 = Options()
    option1.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(executable_path="C:\\Driver\\chromedriver.exe", chrome_options=option1)
    context.driver.maximize_window()
    context.driver.get("https://www.axisbank.com")


@when('click on login button')
def openLoginPage(context):
    login = context.driver.find_element_by_xpath("//div[@class='loginClk jsloginClk']")
    actions = ActionChains(context.driver)
    actions.move_to_element(login).perform()


@when('click on register button')
def clickButton(context):
    context.driver.find_element_by_xpath("//a[contains(text()[1],'Register')]").click()


@then('I should see Customer Id field')
def verifyField(context):
    context.driver.find_element_by_xpath("//input[@id='FORM_USERINFO_LOGIN_ID_JS1']").send_keys("000000000")


@then('I should see Proceed button')
def verifyProceedButton(context):
    context.driver.find_element_by_xpath("//input[@id='Proceed1']").click()
    context.driver.get_screenshot_as_file("C:\screenshot\error.png")



@then('I should see back button')
def verifyBackButton(context):
    context.driver.find_element_by_xpath("//a[contains(text(),'Back')]").click()


@then('close browser')
def closeBrowser(context):
    context.driver.close()
