import requests
from lxml import etree


#请求
def request_response(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

#解析
def parse_data(response):
    tree = etree.HTML(response)
    photo_list = tree.xpath('//div[contains(@class,"item")]/img/@data-original')
    name_list = tree.xpath('//div[contains(@class,"item")]//a/text()')
    return photo_list, name_list

#保存
def download(photo_list,name_list):
    for photo,name in zip(photo_list,name_list):
        photo_data = requests.get(f'https:{photo}')
        with open(f'./{name}.jpg','ab') as file:
            file.write(photo_data.content)

#主函数调用
def main():
    response = request_response('https://sc.chinaz.com/tupian/dongman.html')
    photo_list,name_list = parse_data(response)
    download(photo_list,name_list)


if __name__=='__main__':
    main()