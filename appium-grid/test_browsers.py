import threading

from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Testbrowsers():

    def test_edge(self):
        self.driver = webdriver.Edge(executable_path='C:\software\webdrivers\edgedriver_win64\msedgedriver_103.0.1264.62.exe')
        self.driver.get('https://www.baidu.com')

    def test_chrome(self):
        self.driver = webdriver.Chrome(executable_path='C:\software\webdrivers\chromedriver_103.0.5060.134.exe')
        self.driver.get('https://www.baidu.com')

    def test_seleniumgrid(self):
        # 将节点和浏览器名以字典的形式存储
        self.nodes = {
            'http://localhost:4445/wd/hub': 'MicrosoftEdge',
            'http://localhost:4446/wd/hub': 'chrome'
            # 'http://localhost:4448/wd/hub': 'firefox',
            # 'http://localhost:4447/wd/hub': 'internet explorer'
        }
        # 通过遍历字典中的节点和浏览器，分别去执行下面的用例
        for host, browser in self.nodes.items():
            print(host, browser)
            capabilities = {
                'browserName': browser,
                'version': '',
                # 'platform': 'WINDOWS'
                'platform': 'ANY'
            }

            self.driver = webdriver.Remote(command_executor=host, desired_capabilities=capabilities)

            self.driver.get("https://www.baidu.com")
            self.driver.find_element(By.ID,'kw').send_keys('selenium')
            self.driver.find_element(By.ID,'su').click()

            time.sleep(2)
            self.driver.quit()

    def test_seleniumgrid_thread(self):
        # 传入节点数据，执行测试用例
        def run_case(host, browser):
            capabilities = {
                'browserName': browser,
                'version': '',
                'platform': 'ANY'
            }
            driver = webdriver.Remote(
                command_executor=host,
                desired_capabilities=capabilities
            )

            driver.get("https://www.baidu.com")
            driver.find_element(By.ID, 'kw').send_keys('selenium')
            driver.find_element(By.ID, 'su').click()

            time.sleep(2)
            driver.quit()
        # 将节点和浏览器名以字典的形式存储
        nodes = {
            # 远程主机 4445 端口节点运行 edge 浏览器
            'http://localhost:4445/wd/hub': 'MicrosoftEdge',
            # 远程主机 4446 端口节点运行 chrome 浏览器
            'http://localhost:4446/wd/hub': 'chrome',
            # 本地主机 4447 端口节点运行 IE 浏览器
            # 'http://192.168.**.**:4447/wd/hub': 'internet explorer',
            # 本地主机 4448 端口节点运行 firefox 浏览器
            # 'http://192.168.**.**:4448/wd/hub': 'firefox'
        }
        threads = []
        for host, browser in nodes.items():
            print(host, browser)
            th = threading.Thread(target=run_case, args=(host, browser))
            th.start()
            threads.append(th)

        for t in threads:
            t.join()