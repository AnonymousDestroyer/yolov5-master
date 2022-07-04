# -*- coding: utf-8 -*-
# @Time    : 2022/6/30 1:03
# @Author  : Yujin Wang


from pdf2image import convert_from_path
pdf_path = 'D:\PycharmProjects\yolov5-master\data\pdfs/01 2022动力电池负极材料行业概览.pdf'
pages = convert_from_path(pdf_path, 500)

# 保存
for page_index,page in enumerate(pages):
    page.save('pdfs/out_{}.jpg'.format(page_index), 'JPEG')


