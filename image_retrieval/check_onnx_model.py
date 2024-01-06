#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：cxy 
@File    ：check_onnx_model.py
@IDE     ：PyCharm 
@Author  ：haoran
@Date    ：2023/4/28 18:01 
'''

from model_zoo.feat_extractor import FeatExtractor
from apis.infer_faiss import infer
import time
import os

def inference(img, model_path):
    """

    @param db:
    @param img:
    @param model_path:
    @param detector_model_path:
    @param topk:
    @param topd:在检索中返回topd distance，一般设置为样本库的数量通过db.__len__() 获取
    @return:
    """
    method = FeatExtractor(model_path=model_path)
    # samples = db.get_samples()
    # index = db.get_index()
    query = method.make_single_sample(img)
    # print(query['hist'])
    print(len(query['hist']))
    # parameters
    # s1 = time.time()
    # top_cls, std_result = infer(query, samples=samples, index=index, topk=topk,topd=topd, thr=thr)
    # e1 = time.time()
    # print('infer 用时{}'.format((e1-s1)))
    # print('topk possible predicted classes:', top_cls)
    # print('按阈值过滤后的结果:', std_result)
    # return top_cls, std_result


if __name__ == '__main__':

    # database is saved in ./database
    project_root = os.getcwd()
    model_path = os.path.join(project_root, 'model_zoo/checkpoint/res18-imagenet-holiday-partial.onnx')
    # detector_model_path = os.path.join(project_root, 'model_zoo/checkpoint/pipeline-small-秤.mnn')

    # db = Database(img_dir='database', cache_dir='./cache')
    # db.connect_db()
    # topd = int(db.__len__())
    # img = '/Users/musk/Desktop/实习生工作/COCO-Hand/COCO-Hand-S/COCO-Hand-S_Images/000000000459.jpg'
    # img = '/Users/musk/Desktop/实习生工作/dataset/cargoboat_split/train_img/ship16.jpg'

    img = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/retrieval-DL-based/cache/tmp_img.jpg'
    inference(img, model_path)