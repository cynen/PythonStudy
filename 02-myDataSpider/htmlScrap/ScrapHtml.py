
from bs4 import BeautifulSoup
import  requests
import json
import urllib.request

#获取一整页的数据
def get_one_page(url):
    response = requests.get(url=url)
    if response.status_code != 200:
        return "";
    return response.text


# 解析一整页的数据
# 返回列表，如果是列表页面，返回所有的列表。
def get_list(html):
    soup = BeautifulSoup(html);
    return soup.select(".video");

# 获取页面图片
def download_img(img_url, api_token):
    if img_url.startswith("http:"):
        print("img_url不用处理。。。")
    else:
        img_url = "http:" + img_url

    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        image_name = img_url.split("/",-1);
        filename = "F:\\myth\\pic\\"+ image_name[-1];
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"


# 获得下一页，返回html页面。
# 获取指定页的内容
def get_next_page(url):
    return get_one_page(url);



if __name__=="__main__":
    baseurl = "http://p42u.com/cn/vl_genre.php?g=p4";
    html = get_one_page(baseurl);
    for img in get_list(html):
        imgurl = img.a["href"].split(".", -1)[-1]
        # print(imgurl)
        page = get_one_page("http://p42u.com/cn" + imgurl)
        soup = BeautifulSoup(page)
        real_img = soup.select("#video_jacket_img")[0]
        print(real_img["src"])
        download_img(real_img["src"],"");