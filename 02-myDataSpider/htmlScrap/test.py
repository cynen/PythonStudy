from bs4 import  BeautifulSoup


if __name__ == "__main__":

    baseurl = "http://p42u.com/cn/vl_genre.php?g=p4";
    html = get_one_page(baseurl);
    soup = BeautifulSoup(html)
    list = soup.select(".video")
    print(list[0])
    print(list[0].a["href"].split(".", -1))
    print(list[0].img["src"])
    # http://p42u.com/cn/?v=javli63psi
    ext = list[0].a["href"].split(".", -1)[-1]
    print(ext)

    html2 = get_one_page("http://p42u.com/cn" + ext)

    soup2 = BeautifulSoup(html2)
    real_img = soup2.select("#video_jacket_img")[0]
    print(real_img)
    print(real_img["src"])


    print("1111111")
    url = "//pic.image.cn"
    if url.startswith("http"):
        print("1111111111111")
    else:
        print("http:"+url)

