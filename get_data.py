import requests
from lxml import etree
import json
import openpyxl
url = "https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_pc_3"
response = requests.get(url)
# print(response.text)

# 生成HTML对象
html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
result = result[0]
# json.loads() 将字符串转变为字典
result = json.loads(result)

# 创建工作簿
wb = openpyxl.Workbook()
# 创建工作表
ws = wb.active
ws.title = "国内疫情"
ws.append(['省份','累计确诊','死亡','治愈','现有确诊','累计确诊增量','死亡增量','治愈增量','现有确诊增量'])

# print(result['component'][0]['caseList'])
result_in = result['component'][0]['caseList']   #国内疫情
result_out = result['component'][0]['globalList']  #国外疫情
for each in result_in:
    temp_list = [each['area'],each['confirmed'],each['died'],each['crued'],each['curConfirm'],each['confirmedRelative'],
               each['diedRelative'],each['curedRelative'],each['curConfirmRelative']]
    for i in range(len(temp_list)):
        if temp_list[i] == '':
            temp_list[i]=='0'
    ws.append(temp_list)
    # print(each)
    # print('*'*50+'\n')
#     国外疫情
for each in result_out:
    sheet_title = each['area']
    #创建新的工作表
    ws_out = wb.create_sheet(sheet_title)
    ws_out.append(['国家','累计确诊','死亡','治愈','现有确诊','累计确诊增量'])
    for country in each['subList']:
        temp_list = [country['country'],country['confirmed'],country['died'],country['crued'],
                     country['curConfirm'],country['confirmedRelative']]
        for i in range(len(temp_list)):
            if temp_list[i] == '':
                temp_list[i] == '0'
        ws_out.append(temp_list)
wb.save('./data.xlsx')

'''
area   省份
city   城市
died   死亡人数
crued  治愈人数
confirmedRelative  累计确诊人数
cruedRelative   治愈增量
curConfirm   现有确诊人数
curConfirmRelative  现有确诊数量
diedRelative  死亡增量
'''