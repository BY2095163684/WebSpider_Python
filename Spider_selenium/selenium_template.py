from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging      #日志输出


#设置日志输出形式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')


class Crawler_test(object):
    #初始化浏览器对象
    #将注释取消,就是防检测"自动化测试软件",加上浏览器无头模式
    def __init__(self) -> None:
        try:
            option = webdriver.ChromeOptions()
            # option.add_experimental_option('excludeSwitches',['enable-automation'])
            # option.add_experimental_option('useAutomationExtension',False)
            option.add_argument('--headless')
            self.browser = webdriver.Chrome(options=option)
            # self.browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
            #     'source':'Object.defineProperty(navigator, "webdriver",{get: () => undefined})'
            # })
            self.wait = WebDriverWait(self.browser,10)
            logging.info('初始化浏览器成功')
        except Exception:
            logging.error('初始化浏览器失败')

    #查找输入标签并输入表单
    def find_input(self, target_locator:tuple, some:str) -> None:
        some_input = self.wait.until(EC.presence_of_element_located(locator=target_locator))
        some_input.send_keys(some)

    #查找按钮标签并点击
    def find_button(self, target_locator:tuple) -> None:
        a_button = self.wait.until(EC.presence_of_element_located(locator=target_locator))
        try:
            a_button.click()
        except Exception:
            # 执行js语句实现点击操作
            self.browser.execute_script("arguments[0].click();", a_button)

    #切换选项卡
    def change_window(self, page:int) -> None:
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[page-1])


if __name__=='__main__':
    browser = Crawler_test()
    browser.browser.get('')
    #......
    browser.browser.quit()