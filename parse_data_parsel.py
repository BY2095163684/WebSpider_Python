from parsel import Selector


if __name__=='__main__':
    #请求得到的html文本
    html_text = ''

    #声明一个Selector对象用于解析,向其传入html_text参数(请求得到的html文本)
    selector = Selector(text=html_text)

    #CSS选择器,返回SelectorList对象列表
    selectorlist = selector.css('.sq')

    #Xpath,返回SelectorList对象列表
    selectorlist = selector.xpath('//li/a[contains(@class,"sq")]')

    #也支持正则
    selectorlist = selector.re('link.*')

    #SelectorList对象列表可遍历,再嵌套使用Xpath或CSS选择器
    for selector in selectorlist:
        #get()获取第一个内容,getall()获取所有内容
        result = selector.xpath('.//text()').get()
        result = selector.xpath('.//@src').getall()
