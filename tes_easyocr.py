# -*- coding: utf-8 -*-
# @Time    : 2022/7/2 3:31
# @Author  : Yujin Wang
import os

import easyocr

# 设置识别中英文两种语言
reader = easyocr.Reader(['ch_sim', 'en'], gpu=True)  # need to run only once to load model into memory
root_path = 'runs/detect/exp18/crops/title/0001_images_33_0.jpg'
# ocr_img_path = [root_path+nam for nam in list(os.listdir('runs/detect/exp18/crops/title'))]
result = reader.readtext(root_path, detail=0)[0]
print(result)