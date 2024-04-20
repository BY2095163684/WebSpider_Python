import asyncio
import aiohttp
from parsel import Selector
import json

# 异步获取指定网页html源码
async def get_html(url):
    #创建客户端(Client)请求对象session
    async with aiohttp.ClientSession() as session:
        #接收响应对象response
        async with session.get(url) as response:
            #异步获取的response写入(text)是协程(coroutine)
            html = await response.text()
            return html
        
# ↑↑↑以上函数↑↑↑ 多处使用with as的上下文管理器
# 在异步编程中,资源管理尤为重要,因为异步任务的开始和结束不像同步代码那样容易追踪
# 上下文管理器提供了一种优雅的方式来确保资源在正确的时间被分配和释放
# 这对于保持程序的健壮性和避免难以调试的资源泄露问题至关重要

# 异步获取多个网页的源码并返回其组成的列表
async def get_img():
    # 使用asynio.gather()把传入的多个函数参数(coroutines)包装为tasks,实现"排队"(异步)执行
    htmls = await asyncio.gather(
        # 列表前加"*"是将列表解包为一个个独立的参数
        *[get_html(f'https://sc.chinaz.com/tupian/dongman_{page}.html') for page in range(2,11)]
        )
    return htmls

# parsel解析,json保存
def download(htmls):
    img_data = []
    for html in htmls:
        selector = Selector(text=html)
        img_list = selector.xpath('//div[contains(@class,"tupian-list")]/div[contains(@class,"item")]/img/@data-original').getall()
        name_list = selector.xpath('//div[contains(@class,"tupian-list")]/div[contains(@class,"item")]//a/text()').getall()
        for img,name in zip(img_list,name_list):
            img_data.append({
                'img_url':'https:' + img,
                'name':name
            })
    with open('./test.json','a',encoding='utf-8') as file:
        file.write(json.dumps(img_data,ensure_ascii=False,indent=2))


if __name__=='__main__':
    # asyncio.run创建event_loop,指派执行coroutine或task
    htmls = asyncio.run(get_img())
    download(htmls)