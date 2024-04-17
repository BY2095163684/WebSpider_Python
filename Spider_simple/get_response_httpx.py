# PowerShell依次执行 pip install httpx, pip install httpx[http2]
# 这样就能同时安装httpx及其对HTTP/2.0的支持模块
# 语法与requests几乎一样

import httpx


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

    #Get请求
    response = httpx.get(target_url,params=param,headers=header,proxies=proxy)

    #POST请求
    response = httpx.post(url=target_url, data=target_data, headers=header, proxies=proxy)


    #声明Client对象以支持HTTP/2.0,否则仍是HTTP/1.1
    with httpx.Client(http2=True) as client:
        response = client.get(target_url,headers=header)

    print(response.status_code)    #HTTP状态码
    print(response.headers)    #响应头
    print(response.text)    #返回值文本形式