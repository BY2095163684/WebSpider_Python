## 想成为爬虫高手,至少先踏进牢门半步 (?)

### 简单爬虫

最基础的爬虫: __请求__ + __解析__ + __保存__.

--> *[分析 + 案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/)*
__________________________________
### 异步爬虫

协程是一种用户态内的上下文切换技术,也被称为微线程,它通过一个线程实现代码块之间的相互切换执行.
简单来说,在单进程单线程里,遇到耗时操作(尤其是网络请求)时,能够先挂起这个耗时操作,先去做别的事,充分利用资源.
Python标准库中的模块`asyncio`,与关键字`async`/`await`配合能更方便地编写协程代码.

Python爬虫中`asyncio`与`aiohttp`(异步HTTP网络模块)联动后可以实现 __异步爬虫__.

--> *[分析 + 案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_asyncio/)*
__________________________________
### selenium自动化

如今五花八门的反爬手段,如果我们仅仅使用requests,肯定经常被屏蔽,最为经典的就是js渲染反爬

应对这种情况,要么逆向js逻辑,要么就是使用像 __selenium__ 这类自动化测试工具

逆向js可不是简单操作,所以先学着用 __selenium__

--> *[分析 + 案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_selenium/)*