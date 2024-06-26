## 简单爬虫

一般包含三步: __请求__, __解析__, __保存__.

- 请求
    - 访问网页以获取响应的数据
    - *[requests](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/get_response_requests.py)*: 简单好用的HTTP请求库
    - *[httpx](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/get_response_httpx.py)*: 此库用于解决HTTP/2.0请求, API与requests相似

- 解析
    - 从请求得到的数据解析提取有用数据
    - *[lxml](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/parse_data_lxml.py)*: 利用Xpath语法,修正并解析HTML文本
    - *[parsel](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/parse_data_parsel.py)*: Xpath和CSS选择器都可用

- 保存
    - 将解析得到的数据下载至本地
    - *[TXT文本文件存储](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/save_data_txt.py)*: 最原始的文本
    - *[JSON文件存储](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/save_data_json.py)*: 更为严格清晰的格式,返回的是json对象时使用

*[简单小案例_1](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/test_1.py)*: requests + lxml 爬取站长素材第一页动漫图片

*[简单小案例_2](https://github.com/BY2095163684/WebSpider_Python/blob/main/Spider_simple/test_2.py)*: requests + parsel + json 爬取网站第一页电影排名信息