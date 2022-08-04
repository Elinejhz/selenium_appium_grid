import logging
import os
import threading

from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
import time
from selenium.webdriver.common.by import By

PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))

class TestAppiumGrid():

    def setuop(self):
        pass

    def teardown(self):
        pass

    def test_appiumgrid(self):
        # 将节点和浏览器名以字典的形式存储
        self.nodes = {
            'http://localhost:4447/wd/hub': {
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': '127.0.0.1:7555',
            },
            'http://localhost:4448/wd/hub': {
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': '192.168.56.102:5555',
            }
            # 'http://localhost:5555/wd/hub': 'firefox',
            # 'http://localhost:5556/wd/hub': 'internet explorer'
        }
        # 通过遍历字典中的节点和浏览器，分别去执行下面的用例
        for host, device_info in self.nodes.items():
            print(host, device_info)
            desired_caps = {
                'platformName': device_info['platformName'],
                'platformVersion': device_info['platformVersion'],
                'deviceName': device_info['deviceName'],
                "app": PATH("./test-app.apk"),
                # 声明中文
                "unicodeKeyboard": 'True',
                # 声明中文，否则不支持中文
                "resetKeyboard": 'True',
                # 执行时不重新安装包
                'noReset': 'True',
            }
            self.driver = webdriver.Remote(command_executor=host, desired_capabilities=desired_caps)

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
            input_field = self.driver.find_element(AppiumBy.ID, 'name_input')
            time.sleep(1)
            input_field.clear()
            input_field.send_keys('Appium User')
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Send me your name!\")").click()
            self.driver.implicitly_wait(4)
            if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"This is my way of saying hello\")").is_displayed():

                self.driver.find_element(AppiumBy.ID, "goBack").click()

            time.sleep(2)
            self.driver.quit()

    def test_appium_grid(self):
        # 将节点和浏览器名以字典的形式存储
        # self.nodes = {
        #     'http://192.168.56.2:4447/wd/hub': {
        #         'platformName': 'Android',
        #         'platformVersion': '6.0',
        #         'deviceName': '127.0.0.1:7555',
        #     },
        #     'http://192.168.56.2:4448/wd/hub': {
        #         'platformName': 'Android',
        #         'platformVersion': '6.0',
        #         'deviceName': '192.168.56.102:5555',
        #     }
        #     # 'http://localhost:5555/wd/hub': 'firefox',
        #     # 'http://localhost:5556/wd/hub': 'internet explorer'
        # }
        # 通过遍历字典中的节点和浏览器，分别去执行下面的用例
        # for host, device_info in self.nodes.items():
        #     print(host, device_info)
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': '127.0.0.1:7555',
            "app": PATH("./test-app.apk"),
            # 声明中文
            "unicodeKeyboard": 'True',
            # 声明中文，否则不支持中文
            "resetKeyboard": 'True',
            # 执行时不重新安装包
            'noReset': 'True',
            'chromedriverExecutable': 'C:\software\webdrivers\chromedriver_2.20.353145.exe',
        }
        self.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
        input_field = self.driver.find_element(AppiumBy.ID, 'name_input')
        time.sleep(1)
        input_field.clear()
        input_field.send_keys('Appium User')
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Send me your name!\")").click()
        self.driver.implicitly_wait(4)
        if self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                 "new UiSelector().text(\"This is my way of saying hello\")").is_displayed():

            self.driver.find_element(AppiumBy.ID, "goBack").click()

        time.sleep(2)
        self.driver.quit()

    def test_appiumgrid_thread(self):
        # 传入节点数据，执行测试用例
        def run_case(self, host, browser):
            self.desired_caps = {
                'platformName': browser['platformName'],
                'platformVersion': browser['platformVersion'],
                'deviceName': browser['deviceName'],
                "udid": browser['udid'],
                "app": browser['app'],
                # 声明中文
                "unicodeKeyboard": browser['unicodeKeyboard'],
                # 声明中文，否则不支持中文
                "resetKeyboard": browser['resetKeyboard'],
                # 执行时不重新安装包
                'noReset': browser['noReset'],
                'chromedriverExecutable': browser['chromedriverExecutable'],
            }
            self.driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=self.desired_caps
            )
            # self.driver = webdriver.Remote('http://localhost:4448/wd/hub', desired_caps)

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
            # time.sleep(3)
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
            self.driver.find_element(AppiumBy.XPATH,
                                     '//android.widget.Button[@content-desc="Send me your name!"]').click()
            # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send me your name!").click()
            # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
            # self.driver.implicitly_wait(4)
            print(self.driver.contexts)
            time.sleep(1)
            # if(driver.find_element(AppiumBy.XPATH,
            #                        '//android.view.View[@content-desc="This is my way of saying hello"]')
            #         .is_displayed()):
            #     driver.find_element(AppiumBy.ID, "goBack").click()
            if(self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"This is my way of saying hello\")").is_displayed()):

                self.driver.find_element(AppiumBy.ID, "goBack").click()
            logging.info("test finish!")
            self.driver.quit()
        # 将节点以字典的形式存储
        nodes = {
            # 4447端口开启appium服务
            'http://localhost:4447/wd/hub': {
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
            },
            # 4448端口开启appium服务
            'http://localhost:4448/wd/hub': {
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
            },
        }

        threads = []
        for host, browser in nodes.items():
            print(host, browser)
            th = threading.Thread(target=run_case, args=(self, host, browser))
            th.start()
            threads.append(th)

        for t in threads:
            t.join()

    def test_appiumgrid_thread2(self):
            # 将节点以字典的形式存储
        nodes = {
            # 4447端口开启appium服务
            'http://localhost:4447/wd/hub': {
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
            },
            # 4448端口开启appium服务
            'http://localhost:4448/wd/hub': {
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
            },
        }

        for host, browser in nodes.items():
            print(host, browser)
            # 传入节点数据，执行测试用例
            desired_caps = {
                'platformName': browser['platformName'],
                'platformVersion': browser['platformVersion'],
                'deviceName': browser['deviceName'],
                "udid": browser['udid'],
                "app": browser['app'],
                # 声明中文
                "unicodeKeyboard": browser['unicodeKeyboard'],
                # 声明中文，否则不支持中文
                "resetKeyboard": browser['resetKeyboard'],
                # 执行时不重新安装包
                'noReset': browser['noReset'],
                'chromedriverExecutable': browser['chromedriverExecutable'],
            }
            self.driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=desired_caps
            )
            # self.driver = webdriver.Remote('http://localhost:4448/wd/hub', desired_caps)

            self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "buttonStartWebviewCD").click()
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
            self.driver.find_element(AppiumBy.XPATH,
                                     '//android.widget.Button[@content-desc="Send me your name!"]').click()
            # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Send me your name!").click()
            # self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"Send me your name!\")").click()
            # self.driver.implicitly_wait(4)
            print(self.driver.contexts)
            time.sleep(1)
            self.assertTrue(self.driver.find_element(AppiumBy.XPATH,
                                                     '//android.view.View[@content-desc="This is my way of saying hello"]').is_displayed())
            # self.assertTrue(self.driver.find_element_by_android_uiautomator("new UiSelector().text(\"This is my way of saying hello\")").is_displayed())
            self.driver.find_element(AppiumBy.ID, "goBack").click()

            time.sleep(2)
            self.driver.quit()
