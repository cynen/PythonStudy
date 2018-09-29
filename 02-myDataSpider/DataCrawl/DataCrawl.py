#coding=utf-8
import requests
import pandas as pd
import time
'''
    数据爬取

'''

#爬取数据的URL
base_url = "http://m.maoyan.com/mmdb/comments/movie/1200486.json?_v_=yes&offset="


#爬取每一页的评论
def crawl_one_page_data(url):
    #简单反扒.
    headers = {
        "User - Agent": "Mozilla / 5.0(Windows NT 6.2;WOW64) AppleWebKit / 537.36(KHTML, likeGecko)"
    }
    response = requests.get(url,headers = headers)

    #异常
    if  response.status_code != 200:
        return  []
    return response.json()

#解析数据,返回的是一个数组. [id,...]
def parse(data):
    #print("开始解析数据:"+str(data))
    #result = []
    comments = data.get("cmts")

    if not comments:
        return []
    #生成器,避免内存溢出?
    for cm in comments:
        yield [cm.get("id"),
               cm.get("time"),
               cm.get("score"),
               cm.get("cityName"),
               cm.get("nickName"),
               cm.get("gender"),
               cm.get("content"),
               cm.get("userId"),
               cm.get("userLevel")
               ]

#爬取影评,返回的是一个数组[[],[]...]
def crawl_file_review(total_num = 10):
    data = []
    print(total_num)
    for i in range(0,total_num):
        url = base_url + str(i*15)
        print("解析第{}页".format(i+1))
        crawl_data = crawl_one_page_data(url)
        if crawl_data :
            data.extend(parse(crawl_data))
    return  data


#data = crawl_one_page_data(base_url)
#print(data)

#实际爬的条数为  100*15
start = time.time()
df = pd.DataFrame(crawl_file_review(400),
                  columns=["id","time","score","cityName","nickName","gender","content","userId","userLevel"]);

# xls支持utf-8编码格式. csv不支持.
df.to_csv("F:\\我不是药神_全量.xls",encoding ='utf_8_sig')
end = time.time()
print(end - start)

#做视图处理


