from lxml import etree


if __name__=='__main__':
    #请求得到的html文本
    html_text = ''

    #声明HTML类对象以进行解析
    tree = etree.HTML(text=html_text)

    #也可以解析本地文件
    tree = etree.parse(source='./text.html',parser=etree.HTMLParser())

    #使用Xpath获取所有li节点下的a节点,返回Element类型的列表
    result = tree.xpath('//li/a')

    #在上面的基础上,筛选属性class等于"sq"的a节点
    result = tree.xpath('//li/a[@class="sq"]')

    #contains匹配多值属性class,and可进行多个属性匹配
    result = tree.xpath('//li/a[contains(@class,"sq") and @name="item"]')

    #获取对应节点内的文本
    result = tree.xpath('//li/a[@class="sq"]/text()')

    #获取对应节点的src属性
    result = tree.xpath('//li/a[@class="sq"]/@src')


#Xpath语法可参考 https://www.runoob.com/xpath/xpath-syntax.html