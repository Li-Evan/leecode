import requests
import pandas as pd
from lxml import etree

res = requests.get('http://www.csres.com/notice/55878.html')
res_elements = etree.HTML(res.text)
table = res_elements.xpath('//table[@id="table1"]')
table = etree.tostring(table[0], encoding='utf-8').decode()

df = pd.read_html(table, encoding='utf-8', header=0)[0]
results = list(df.T.to_dict().values())  # 转换成列表嵌套字典的格式

df.to_csv("std.csv", index=False)