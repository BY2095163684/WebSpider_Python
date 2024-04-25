### selenium自动化

__selenium__ 的原理简单说就是打开浏览器进行自动操作,所以任何正常浏览器能显示的内容,都可以使用 __selenium__ 进行爬取,做到"所见即所爬"

--> *[一个分析案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_selenium/selenium_basic.py)*
了解常用 __selenium__ 方法

不过当对浏览器的操作变多时,直接写自动化程序就会把代码堆成一大坨(题主爬知网时就试过,一大团代码属实难看).

所以建议创建一个类,将多次操作(如找输入和按钮标签节点)封装成类方法,直接调用就行了

--> *[一个模板案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_selenium/selenium_template.py)*
封装了常用方法

--> *[一个实战案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_selenium/selenium_test.py)*
使用模板爬取小说信息