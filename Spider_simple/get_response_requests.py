import requests


if __name__=='__main__':
    #目标URL地址
    target_url = ''

    #URL参数
    param = {
        '':''
    }

    #请求数据(请求体,常用于POST请求,GET请求留空)
    target_data = {
        '':''
    }

    #请求头
    header ={
        '':''
    }

    #代理池
    proxy ={
        '':''
    }

    #GET请求
    response = requests.get(url=target_url, params=param, headers=header, proxies=proxy)

    #POST请求
    response = requests.post(url=target_url, data=target_data, headers=header, proxies=proxy)

    print(type(response))    #URL响应返回值为Response类型的对象
    print(response.status_code)    #HTTP状态码
    print(response.text)    #返回值文本形式
    print(response.content)    #返回值二进制形式
    print(response.cookies)    #Cookie的类型是RequestsCookieJar

    #Session对象保持连接,模拟同一会话,解决了重复访问Cookie不一样的问题
    with requests.Session() as session:
        response = session.get(url=target_url, params=param, headers=header, proxies=proxy)