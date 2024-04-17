if __name__=='__main__':
    #解析得到的文本数据
    result = ''

    #创建一个txt文件直接写进去
    with open('./test.txt','w',encoding='utf-8') as file:
        file.write(result)

    #可以将解析得到的数据转为字节码,以二进制写入,更快
    with open('./test.txt','wb') as file:
        file.write(result)
    #而且涉及图片或视频的爬取,一般是把二进制数据写入对应拓展名的文件