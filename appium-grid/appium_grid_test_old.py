# coding=utf-8
import unittest
from appium import webdriver
import time
import os

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


class AndroidSimpleTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '192.168.56.101:5555',
            "udid": "192.168.56.101:5555",
            "app": PATH("./test-app.apk"),
            # 声明中文
            "unicodeKeyboard": 'True',
            # 声明中文，否则不支持中文
            "resetKeyboard": 'True',
            # 执行时不重新安装包
            'noReset': 'True',
            'chromedriverExecutable': 'C:\software\webdrivers\chromedriver_2.20.353145.exe',
        }
        # desired_caps = {
        #     'platformName': 'Android',
        #     'platformVersion': '6.0',
        #     'deviceName': '127.0.0.1:7555',
        #     "udid": "127.0.0.1:7555",
        #     "app": PATH("./test-app.apk"),
        #     # 声明中文
        #     "unicodeKeyboard": 'True',
        #     # 声明中文，否则不支持中文
        #     "resetKeyboard": 'True',
        #     # 执行时不重新安装包
        #     'noReset': 'True',
        # }
        # self.driver = webdriver.Remote('http://localhost:4447/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://localhost:4448/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
        # search_locator = (AppiumBy.ID, 'name_input')
        # WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(search_locator))
        time.sleep(3)
        print(self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_io.selendroid.testapp")
        input_field = self.driver.find_element(AppiumBy.ID, 'name_input')
        # input_field = self.driver.find_element(AppiumBy.XPATH, '//android.webkit.WebView[@content-desc="Say Hello Demo"]/android.view.View[2]/android.widget.EditText')
        time.sleep(3)
        input_field.clear()
        input_field.send_keys('Appium User')
        print(self.driver.contexts)
        self.driver.switch_to.context("NATIVE_APP")
        time.sleep(3)
        self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Send me your name!"]').click()
        # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send me your name!").click()
        # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
        # self.driver.implicitly_wait(4)
        print(self.driver.contexts)
        time.sleep(1)
        self.assertTrue(self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="This is my way of saying hello"]').is_displayed())
        # self.assertTrue(self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"This is my way of saying hello\")").is_displayed())
        self.driver.find_element(AppiumBy.ID, "goBack").click()


if __name__ == '__main__':
    unittest.main()
