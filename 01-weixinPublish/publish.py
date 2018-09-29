

from PIL import Image
import os

'''
    填充图片:
    将一个图片修正为正方形.
    
'''
def fill_image(image):
    width,height = image.size
    new_image_length = width if width > height else height
    new_image = Image.new(image.mode,(new_image_length,new_image_length),color="white")
    #填充图片
    #原图宽大于高.
    if width > height:
        new_image.paste(image,(0,int((new_image_length-height)/2)))
    else:
        new_image.paste(image,(int((new_image_length -width)/2),0))
    return new_image

'''
    切图,传入的图片切成9块.
'''
def cut_image(image):
    # image.crop() 传入一个元祖. 左上右下
    box_list = []
    # 坑爹, Image.size方法返回的是一个元祖.(width,height)
    width,height = image.size

    item_width = int(width/3)

    for i in range(3):
        for j in range(3):
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)

    image_list = [image.crop(box) for box in box_list]
    return image_list

def save_image(image_list):
    index = 1
    savePath = "F:/data/Pic/高逼格/"
    if not os.path.exists(savePath):
        os.makedirs(savePath)
    for image in image_list:
        #确保这个文件夹存在,不存在需要创建.
        image.save(savePath + str(index)+"A.jpg","PNG")
        index += 1


if __name__=="__main__":
    image = Image.open("F:/data/Pic/0438.jpg")
    image = fill_image(image)
    image_list = cut_image(image)
    save_image(image_list)
    print("执行完成....")







