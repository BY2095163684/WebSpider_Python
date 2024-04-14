import json


if __name__=='__main__':
    #解析得到的json文本数据
    result = ""

    #loads将json文本转为json对象(列表字典结合)
    content = json.loads(result)

    #dumps将json对象转为json文本
    content = json.dumps(content)

    #写入必须以文本形式
    with open('./test.json','w',encoding='utf-8') as file:
        file.write(json.dumps(content,ensure_ascii=False,indent=2))