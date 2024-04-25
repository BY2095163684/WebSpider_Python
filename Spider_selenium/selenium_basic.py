from selenium import webdriver      #用于创建浏览器对象
from selenium.webdriver.common.by import By     #用于查找标签节点
from selenium.webdriver.support.wait import WebDriverWait       #用于等待页面加载(显式等待)
from selenium.webdriver.support import expected_conditions as EC        #用于确认指定标签节点已经加载完成


if __name__=='__main__':
    #创建浏览器对象
    browser = webdriver.Chrome()

    #访问网页
    browser.get('')

    #使用xpath查找单个标签节点
    input_or_button = browser.find_element(by=By.XPATH,value='')
    #使用CSS选择器查找多个标签节点
    inputs_or_buttons = browser.find_elements(by=By.CSS_SELECTOR,value='')

    #WebDriverWait对象,指定最长等待时间为10
    wait = WebDriverWait(browser,10)
    #所找标签在10秒内成功加载出来,就返回该标签节点,否则抛出异常
    input_or_button = wait.until(EC.presence_of_element_located((By.XPATH,'')))

    #获取浏览器选项卡列表
    window_list = browser.window_handles
    #转至第二个选项卡
    browser.switch_to.window(window_list[1])

    #当前选项卡网页源码
    response = browser.page_source

    #用完记得关
    browser.close()

# selenium还有很多用法,可以到官网查看