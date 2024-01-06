#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：retrieval-DL-based
@File    ：main_new.py
@IDE     ：PyCharm
@Author  ：haoran
@Date    ：2024/1/5 16:44
'''

import os
import shutil
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from visualize import ImageDisplayApp
from image_retrieval.main_md5_faiss import Retrievaler # 检索模型，包括建数据库，增量学习，实现检索



class ImageFinder:
    def __init__(self, model_type='holidays'):
        self.project_root = os.getcwd()
        self.model_type = model_type # default
        self.retrievaler = Retrievaler(model_type=model_type)

    def func1(self, img_path,topk=10):
        """


        :param img_path: 图片的绝对路径
        :param topk:
        :return: 返回一个dict，包含前端所需要的所有信息
        """
        if os.path.exists(img_path):
            ret = self.retrievaler.retrieval_one_img(img_path,topk)
            return ret
        else:
            return None

    def choice_one_image(self,idx):
        """
        此功能需要结合前端去实现
        :param idx:
        :return:
        """
        return idx


    def inset(self):
        """
        新增一张图片到样本库
        :return:
        """
        self.retrievaler.insert()

    def create_db(self):
        self.retrievaler.create_db()

    def move_img(self,src_path,dst_path):
        shutil.move(src_path,dst_path) # TODO 1: to Check

if __name__ == '__main__':
    finder = ImageFinder(model_type='holidays')

    # visualize
    root = tk.Tk()
    app = ImageDisplayApp(root)
    img_path = app.select_image()
    print(img_path)
    # test func1
    # img_path = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/retrieval-DL-based/image_retrieval/holidays_split/val/bunga/136004.jpg'
    # if img_path == '':
    #     img_path = input('Please give an image path')
    # else:
    #     pass

    result = finder.func1(img_path=img_path)
    print("Retrieval Result：")
    print(result)


    app.show_result(result=result['std_result'])
    root.mainloop()
    ## test append learning
    # finder.inset()
    ##############################################################

