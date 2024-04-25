from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
import time


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s : %(message)s')


class Crawler_test(object):
    def __init__(self) -> None:
        try:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('excludeSwitches',['enable-automation'])
            option.add_experimental_option('useAutomationExtension',False)
            # option.add_argument('--headless')
            self.browser = webdriver.Chrome(options=option)
            self.browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
                'source':'Object.defineProperty(navigator, "webdriver",{get: () => undefined})'
            })
            self.wait = WebDriverWait(self.browser,10)
            logging.info('初始化浏览器成功')
        except Exception:
            logging.error('初始化浏览器失败')

    def find_input(self, target_locator:tuple, some:str) -> None:
        some_input = self.wait.until(EC.presence_of_element_located(locator=target_locator))
        some_input.send_keys(some)

    def find_button(self, target_locator:tuple) -> None:
        a_button = self.wait.until(EC.presence_of_element_located(locator=target_locator))
        try:
            a_button.click()
        except Exception:
            self.browser.execute_script("arguments[0].click();", a_button)

    def change_window(self, page:int) -> None:
        windows = self.browser.window_handles
        self.browser.switch_to.window(windows[page-1])


if __name__=='__main__':
    browser = Crawler_test()
    browser.browser.get('https://www.bigee.cc/')
    browser.find_input((By.XPATH,'/html/body/div[4]/div[1]/div[2]/form/input[1]'),'斗破苍穹')
    browser.find_button((By.XPATH,'/html/body/div[4]/div[1]/div[2]/form/input[2]'))
    time.sleep(5)
    print(browser.browser.page_source)
    browser.browser.quit()