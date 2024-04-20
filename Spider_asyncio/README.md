## 异步爬虫

- 一些概念:
    - __event_loop__: 事件循环,运算核心,面对多个并决定执行某个 __coroutine__ 或 __task__.
    不能自主切换上下文,需要 __coroutine__ 或 __task__ 主动传递控制权.
    - __coroutine__ (或称协程): 具有开始(enter)/暂停(exit)以及任意恢复(resume)执行的能力
        - coroutine object
        - coroutine function (比如 `async def main()` )
    - __awaitables__: 在使用`asyncio`相关函数时，经常可以在文件中看到`awaitables`关键字，这个关键字就代表以下3种Python物件(objects)，也是`await`语法适用的对象：
        - Coroutines
        - Tasks - asyncio.Task
        - Futures - asyncio.Future
    - __tasks__:我们可以将 __task__ 视为是 __coroutine__ 的再包裝
    - __futures__: __task__ 继承自 __future__,因此 __future__ 是相对底层(low-level)的`awaitable`Python物件,用以代表非同步操作的最终结果,一般并不需要自己创造 __future__ 物件进行操作,多以 __coroutine__ 与 __task__ 为主

异步编程通过编写非阻塞的代码,让程序中的一个工作单元与主应用程序线程分开独立运行.在工作单元运行结束后,它会通知主应用程序线程它的运行结果或失败原因.使用异步编程可以提高应用程序的性能和响应能力

例如,在发起网络IO请求时,使用异步方式,调用线程不会同步阻塞等待响应结果.相反,它会在内存中保存请求上下文后立即返回,继续执行其他操作.等网络IO响应结果返回后,再通知业务线程进行处理,异步调用方式提高了线程的利用率,让系统有更多线程资源来处理更多请求

在Python爬虫里,异步多用于请求URL时充分利用网络响应的耗时,比如要请求100个网站,可以让这100个网站同时"排队". `import asyncio` + `import aiohttp` 就可以支持异步请求

--> *[一个分析案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_asyncio/asyncio_basic.py)*
大概了解asyncio异步原理

--> *[一个实战案例](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_asyncio/asyncio_test.py)*
爬取站长素材2~10页动漫图片