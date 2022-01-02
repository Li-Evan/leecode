#coding=utf-8
#老规矩，第12行 Bitcoin.txt换成自己的文件名，19行wordcloud.jpg换成自己的图片名 
#最后一行wordcloud.png')为输出的图片名，你们也可以按自己的需要更换
#注意上面的文件夹都是默认文件夹  在C:/user/你的用户名
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

for i in range(0,1):
    name = "Lecture2{0}".format(i)
    text = open(r'D:\code\python\txt\IntroToLinearDynamicalSystems-{0}.pdf.txt'.format(name),'r',encoding='utf-8').read()#从文件中获取文本
    text = text.lower()    #将文本中的所有大写字母转换为小写字母
    for c in '!"#$%^&*()_+-=@[]{}|\?/<>,.:;~·`、“”‘’':    #替换文本中的所有特殊符号为空格
        text = text.replace(c," ")

    string =  text

    img = plt.imread('7词云专用图.jpg') # 如果你们要用自己的照片  这个就需要换成你们自己的照片
    img_array = np.array(img)

    wc = WordCloud(background_color='white',
                   width=1000,
                   height=800,
                   mask=img_array
                   ).generate(string)
    wc.to_file('{0}-wordcloud.png'.format(name)) #保存图片，图片命名wordcloud.png