
import  pandas as pd
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import matplotlib.pyplot as plt
'''
    生成数据词云
'''



#导入数据.
data = pd.DataFrame(pd.read_csv("F:\\data\\1000.xls"));

#先获取到对应的字段的一个关键字list-->str
comment = jieba.cut(str(data['content']),cut_all=False)
"""
word_generator = jieba.cut_for_search(str(data['content']))
for word in word_generator:
    wordlist.append(word)
"""

#除短小的关键字
wordlist = [k for k in comment if len(k)>1]
print("单词量: "+str(len(wordlist)))
#对分词后的单词,使用join拼成一个字符串.
wl_space_split = " ".join(wordlist)

#导入背景图
backgroud_Image = plt.imread('F:\\data\\西红柿.jpg')

#设置停用词.
stopwords = STOPWORDS.copy()
stopwords.add("电影")
stopwords.add('一部')

#初始化词云对象
wc = WordCloud(#width=1024,height=768,
    background_color='white', # 生成 词云的背景色
    mask=backgroud_Image, #背景图片
    font_path="C:/Windows/Fonts/simkai.ttf",#防止中文乱码,选择本地的ttf文件
    stopwords=stopwords, #停用词.
    max_font_size=300,  #最大单词的size
    scale=3,#画布放大3倍
    random_state=50)

#生成词云
wc.generate_from_text(wl_space_split)

#按照背景颜色生成单词颜色.
imgcolor = ImageColorGenerator(backgroud_Image)
#重新赋值颜色.
plt.imshow(wc.recolor(color_func=imgcolor))
"""
#不使用背景图片的颜色
plt.imshow(wc)
"""
plt.axis('off')#不显示坐标轴
plt.show() #显示词云,此句可要可不要.弹窗显示
wc.to_file('F:/data/normal.jpg')