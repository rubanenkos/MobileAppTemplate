from appium import webdriver

from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "deviceName": "Pixel 2 API 26",
        "platformName": "Android",
        "version": "8.0+",
        "app": "/Users/rubanenko.sergii/PycharmProjects/WikiApp/app_binary/Calculator.apk"
    }
    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()