# -*- coding: utf-8 -*-
# @Time    : 2022/7/4 6:06
# @Author  : Yujin Wang

import json

dic = [{'pdf_name':'0001_哈哈哈','total':2,'results':[{'page_name':'123哈哈哈我们爱上对方交水电费囧.png','type':'chart','title':'ahahha','conference':0.5}]},{}]

with open('tes.json','w',encoding='utf-8')  as obj:
    json.dump(dic,obj,ensure_ascii=False,indent=4)
print('ok')
