#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：retrieval-DL-based 
@File    ：split_Oxford5k.py
@IDE     ：PyCharm 
@Author  ：haoran
@Date    ：2024/1/5 13:41 
'''

import os
import shutil

if __name__ == '__main__':
    data_root = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/oxbuild_images'
    target_folder = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/oxbuild_images_splits'
    if os.path.exists(target_folder):
        pass
    else:
        os.mkdir(target_folder)
    image_list = os.listdir(data_root)
    categories = []
    for idx,name in enumerate(image_list):
        print(idx)
        if name.split('_')[0] not in categories:
            categories.append(name.split('_')[0])
            os.mkdir(os.path.join(target_folder,categories[-1]))
        else:
            pass
        src_path = os.path.join(data_root,name)
        dst_path = os.path.join(target_folder,name.split('_')[0],name)
        shutil.copy(src_path,dst_path)

    print(categories)
    print('The category nums is :',len(categories))

