import logging
import os

from appium import webdriver
import time
import threading

from appium.webdriver.common.appiumby import AppiumBy

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
class TestaooiumGrid():
    def test_appiumgrid(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '192.168.56.102:5555',
            "udid": "192.168.56.102:5555",
            "app": PATH("./test-app.apk"),
            # 声明中文
            "unicodeKeyboard": 'True',
            # 声明中文，否则不支持中文
            "resetKeyboard": 'True',
            # 执行时不重新安装包
            'noReset': 'True',
            'chromedriverExecutable': 'C:\software\webdrivers\chromedriver_2.20.353145.exe',
        }

        desired_caps2 = {
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
        def task1():
            driver = webdriver.Remote('http://localhost:4447/wd/hub', desired_caps)
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
            time.sleep(3)
            print(driver.contexts)
            driver.switch_to.context("WEBVIEW_io.selendroid.testapp")
            input_field = driver.find_element(AppiumBy.ID, 'name_input')
            # input_field = self.driver.find_element(AppiumBy.XPATH, '//android.webkit.WebView[@content-desc="Say Hello Demo"]/android.view.View[2]/android.widget.EditText')
            time.sleep(3)
            input_field.clear()
            input_field.send_keys('Appium User')
            print(driver.contexts)
            driver.switch_to.context("NATIVE_APP")
            time.sleep(3)
            driver.find_element(AppiumBy.XPATH,
                                '//android.widget.Button[@content-desc="Send me your name!"]').click()
            # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send me your name!").click()
            # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
            # self.driver.implicitly_wait(4)
            print(driver.contexts)
            time.sleep(3)
            # if(driver.find_element(AppiumBy.XPATH,
            #                        '//android.view.View[@content-desc="This is my way of saying hello"]')
            #         .is_displayed()):
            #     driver.find_element(AppiumBy.ID, "goBack").click()
            if (driver.find_element(AppiumBy.XPATH,
                                    '//android.view.View[@content-desc="This is my way of saying hello"]').is_displayed()):
                driver.find_element(AppiumBy.ID, "goBack").click()

            logging.info("test finish!")
            driver.quit()

        def task2():
            driver = webdriver.Remote('http://localhost:4448/wd/hub', desired_caps2)
            ##休眠20s等待页面加载完成
            driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
            time.sleep(3)
            print(driver.contexts)
            driver.switch_to.context("WEBVIEW_io.selendroid.testapp")
            input_field = driver.find_element(AppiumBy.ID, 'name_input')
            # input_field = self.driver.find_element(AppiumBy.XPATH, '//android.webkit.WebView[@content-desc="Say Hello Demo"]/android.view.View[2]/android.widget.EditText')
            time.sleep(3)
            input_field.clear()
            input_field.send_keys('Appium User')
            print(driver.contexts)
            driver.switch_to.context("NATIVE_APP")
            time.sleep(3)
            driver.find_element(AppiumBy.XPATH,
                                '//android.widget.Button[@content-desc="Send me your name!"]').click()
            # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send me your name!").click()
            # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
            # self.driver.implicitly_wait(4)
            print(driver.contexts)
            time.sleep(3)
            # if(driver.find_element(AppiumBy.XPATH,
            #                        '//android.view.View[@content-desc="This is my way of saying hello"]')
            #         .is_displayed()):
            #     driver.find_element(AppiumBy.ID, "goBack").click()
            if (driver.find_element(AppiumBy.XPATH,
                                    '//android.view.View[@content-desc="This is my way of saying hello"]').is_displayed()):
                driver.find_element(AppiumBy.ID, "goBack").click()

            logging.info("test finish!")
            driver.quit()

        threads = []
        t1 = threading.Thread(target=task1)
        threads.append(t1)

        t2 = threading.Thread(target=task2)
        threads.append(t2)
        print(threads)
        for t in threads:
            t.start()
        print(threads)