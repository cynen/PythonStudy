import pandas as pd
from pyecharts import Line,Geo,Bar,Overlap,Style
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

#读取数据
f = open("F:/data/aqgy_all.txt",encoding='utf-8')
data = pd.read_csv(f,sep=",",header=None,encoding='utf-8',
                   names=['id','score','cityName','approve','startTime','nickName','content'])

city = data.groupby(['cityName'])
rate_group = city['score']
city_com = city['score'].agg(['mean','count'])

#重设索引
city_com.reset_index(inplace=True)
city_com['mean'] = round(city_com['mean'],2)
'''
#折线+柱图分析
city_main = city_com.sort_values('count',ascending=False)[0:20]
#print(city_main)
attr = city_main['cityName']
v1 = city_main['count']
v2 = city_main['mean']
#print(attr,v1,v2)
line = Line("主要城市评分")
line.add("城市",attr,v2,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    mark_point=['min','max'],xaxis_interval=0,line_color='lightblue',
    line_width=4,mark_point_textcolor='black',mark_point_color='lightblue',
    is_splitline_show=False)

bar = Bar("主要城市评论数")
bar.add("城市",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)

overlap = Overlap()
overlap.add(bar)
overlap.add(line,yaxis_index=1,is_add_yaxis=True)
overlap.render('F:/主要城市评论数_平均分.html')
'''


'''
#还未调试完.
#热力图分析
data_map = [(city_com['cityName'][i],city_com['count'][i]) for i in range(0,city_com.shape[0])]
#print(data_map)
style = Style(title_color="#fff",title_pos = "center",
            width = 1200,height = 600,background_color = "#404a59")

geo = Geo("《爱情公墓》粉丝人群地理位置","数据来源：恋习Python",**style.init_style)

while True:
    try:
        attr,val = geo.cast(data_map)
        geo.add("",attr,val,visual_range=[0,20],
                visual_text_color="#fff",
                symbol_size=20,
                is_visualmap=True,
                is_piecewise=True,
                visual_split_number=4
                )
    except ValueError as e:
        e = str(e)
        e = e.split("No coordinate is specified for ")[1]#获取不支持的城市名
        for i in range(0,len(data_map)):
            if e in data_map[i]:
                data_map.pop[i]
                break

    else:
        break
geo.render('F:/data/爱情公墓.html')

'''









'''



#词云分析
#分词
comment = jieba.cut(str(data['content']),cut_all=False)
#wordlist = [k for k in comment if len(k) > 1] #剔除一个词的评论字.
wordlist = [k for k in comment]
print(len(wordlist))
wl_space_split = " ".join(wordlist)

#导入背景图
backgroud_Image = plt.imread('F:/data/西红柿.jpg')
stopwords = STOPWORDS.copy()
stopwords.add("电影")
#print("STOPWORDS.copy()",help(STOPWORDS.copy()))


wc = WordCloud(#width=1024,height=768,
               background_color='white',
              # max_words=200,
                mask=backgroud_Image,
                font_path="C:/Windows/Fonts/simkai.ttf",
               #font_path="C:/Windows/Fonts/simhei.ttf",
                stopwords=stopwords,
               max_font_size=200,
                scale=3,
                random_state=50)

wc.generate_from_text(wl_space_split)
#plt.imshow(wc)
#按照背景颜色生成单词颜色.
imgcolor = ImageColorGenerator(backgroud_Image)
#重新赋值颜色.
plt.imshow(wc.recolor(color_func=imgcolor))

plt.axis('off')#不显示坐标轴
plt.show()
wc.to_file(r'F:/data/aqgy.jpg')

'''