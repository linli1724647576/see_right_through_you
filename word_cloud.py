import openpyxl
from wordcloud import WordCloud
from PIL import Image
import numpy as np
from os import path

def generate_pic(frequency,name,mask):   # frequency为词云的频率，为字典形式,name为生成词云的名字,mask为词云的形状图片
#根据确诊病例数目生成词云
    d = path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d,mask)))
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/STXINGKA.TTF',
                                    mask=alice_mask,
                                    background_color='white',
                                    width = 1920,height=1080)
    wordcloud.generate_from_frequencies(frequency)
    wordcloud.to_file('%s.png'%name)
mask1 = './2.png'
mask2 = './2.png'
#！国内
# 读取数据,根据疫情的严重程度，将不同的省份以词云的形式展示
wb = openpyxl.load_workbook('data.xlsx')
# 获取工作表
ws = wb['国内疫情']
frequency_in = {}
for row in ws.values:
    # print(row)
    if row[0] == '省份':
        pass
    else:
        frequency_in[row[0]] = float(row[1])
print(frequency_in)
# 绘制国内疫情情况词云图
generate_pic(frequency_in,'国内疫情词云图',mask1)

#!国外
# 读取数据,根据疫情的严重程度，将不同的国家以词云的形式展示
frequency_out = {}
sheet_name = wb.sheetnames
for each in sheet_name:
    if "洲" in each:
        ws = wb[each]
        for row in ws.values:
            if row[0] == '国家':
                pass
            else:
                frequency_out[row[0]] = float(row[1])
# 绘制国外疫情情况词云图
generate_pic(frequency_out,'国外疫情词云图',mask2)