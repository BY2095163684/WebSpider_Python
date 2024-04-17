import requests
from parsel import Selector
import json


#请求
def request_response(url):
    response = requests.get(url)
    return response.text

#解析
def parse_data(response):
    selector = Selector(text=response)
    name_list = selector.css('h2::text')\
        .getall()
    detail_list = selector.xpath('//div[contains(@class,"info")]/span[1]/text()')\
        .getall()
    address_list = [address for n,address in enumerate(detail_list) if not n%2]
    result = []
    for name,address in zip(name_list,address_list):
        result.append({
            'name':name,
            'address':address
        })
    return result

#保存
def download(result):
    with open('./test.json','w',encoding='utf-8') as file:
        file.write(json.dumps(result,ensure_ascii=False,indent=2))

#主函数调用
def main():
    response = request_response('https://ssr1.scrape.center')
    result = parse_data(response)
    download(result)


if __name__=='__main__':
    main()