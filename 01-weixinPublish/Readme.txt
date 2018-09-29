
原文:
	https://mp.weixin.qq.com/s/i5Enop8KDuKGPQNhAwhB_g

1. 一个高逼格的说说.
本质就是使用python切图
将一张图片,切成9块一样大小的图片,发布的时候,按照顺序发布,在说说上体现的就是9张.


如下效果:

1   2   3

4   5   6

7   8   9




技术要点:
    主要是用PIL中Image模块的crop()函数来实现.
库:
    PIL
