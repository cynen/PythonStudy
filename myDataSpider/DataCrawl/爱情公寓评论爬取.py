import requests
import time
import json

import os

old = "F:/data/aqold.txt"

#获取一整页的数据
def get_one_page(url):
    response = requests.get(url=url)
    return response.text


#解析一整页的数据
def parse_one_page(html):
    try:
        data = json.loads(html)['cmts'] #python取值.
        for item in data:
            yield {
                "id": item['id'],  # 评论id
                "cityName": item['cityName'],  # 城市
                "content": item['content'],  # 评论内容
                "approve":item['approve'],  # 赞同数
                "nickName": item['nickName'],  # 昵称
                "score": item['score'],  # 评分
                "startTime": item['startTime']  # 评分时间
            }
    except :
        print(html);




#保存 page 页的数据.
def save_data(page):
    #猫眼貌似反扒了,只能抓取1000条数据.
    base_url = "http://m.maoyan.com/mmdb/comments/movie/1175253.json?_v_=yes&offset="

    #获取指定的页数的数据.
    for i in range(page):
        print("准备爬取第{}页".format(i+1))
        #print(base_url+str(i*15))
        html = get_one_page(base_url+str(i*15))
        #print(html)
        for item in parse_one_page(html):
            #print(item)
            with open(old,mode='a',encoding='utf-8') as f:
                f.write(str(item['id'])+","+str(item['score'])+","+item['cityName']+","+str(item['approve'])+","+item['startTime']+","+item['nickName']+","+item['content']+"\r")
        #time.sleep(3) #防止反扒,可以做限制.

#除重:
def remove_duplicate(old,new):
    '''
        读取旧的文件,逐个判断是否存在于新的文件中.重复的旧丢弃.
    '''
    oldF = open(old,'r',encoding='utf-8')
    newF = open(new,'w',encoding='utf-8')

    content_list = oldF.readlines()
    content_already = [] #定义一个存放新数据的数组.

    for item in content_list:
        if item not in content_already:
            newF.write(item+"\r")
            content_already.append(item)




if __name__ == "__main__":
    #old = "F:/data/aqold.txt"
    new = "F:/data/aqnew.txt"
    save_data(66)
    # 除重
    remove_duplicate(old,new)
    print("除重完成,请以{}文件为主".format(new))