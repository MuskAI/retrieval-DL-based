#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：shengxian_retrieval_onnx 
@File    ：visualize_hist.py
@IDE     ：PyCharm 
@Author  ：haoran
@Date    ：2022/4/7 8:04 PM

可视化特征库的特征,为了发现哪些位的值对最终的结果贡献更大
'''
import numpy as np
import math
from construct_database import Database
from pprint import pprint
import matplotlib.pyplot as plt
# plt.rcParams['font.sans-serif'] = ['PingFang']
# plt.rcParams['axes.unicode_minus'] = False
import pinyin


class VisHist:
    def __init__(self, samples):
        self.samples = samples
        pass
        # pprint(samples)
    def get_single_fmap(self, hist,cls,norm_type='linear',fmap_type='2dim'):
        """
        将一个特征可视化成二维图片
        """
        # norm 的方式

        if norm_type == 'linear':

            pass
        elif norm_type == '':
            pass
        else:
            pass

        # 返回方式
        if fmap_type == '2dim':
            w = math.sqrt(hist.shape[0])
            w = math.ceil(w) # 向上取整

            # 空缺平均值q
            padding = [np.mean(hist) for _ in range(w*w - hist.shape[0])]
            hist_2dim = np.hstack((hist,padding))
            hist_2dim = hist_2dim.reshape(w,w)
            plt.imshow(hist_2dim)
            plt.title('The cls is {}'.format(cls))
            plt.show()
        elif fmap_type == '1dim':

            return hist


    def get_single_hist_info(self,hist):
        """
        获取向量的统计特征

        """
        info = {
            '特征维度':hist.shape,
            'max':np.max(hist),
            'min':np.min(hist),
            'mean':np.mean(hist),
            'sum':np.sum(hist),
            'med':np.median(hist),
            'var':np.var(hist)
        }
        # pprint(info)
        return info
    def get_fmap_per_img(self):
        """
        显示每张图片的特征图
        """
        # 获取所有类别
        classes = [i['cls'] for i in self.samples]
        classes = set(classes)
        print('特征库中的类别有{}种，分别是{}'.format(len(classes),classes))

        # 开始遍历所有类别
        for idx, cls_name in enumerate(classes):
            samples_cls = db.find(type='cls',find_key=cls_name)
            # 开始遍历一个类别
            for idx2, sample in enumerate(samples_cls):
                hist = sample['hist']
                cls = sample['cls']
                self.get_single_hist_info(hist=hist)
                self.get_single_fmap(cls=cls, hist=hist)
    def get_fmap_per_cls(self):
        """
        一个类别一张图
        """
        # 获取所有类别
        classes = [i['cls'] for i in self.samples]
        classes = set(classes)
        print('特征库中的类别有{}种，分别是{}'.format(len(classes),classes))

        # 开始遍历所有类别
        plt.figure(figsize=(12.8*2,7.2*2))
        all_hist = np.zeros((500,1280))
        for idx, cls_name in enumerate(classes):

            samples_cls = db.find(type='cls',find_key=cls_name)
            # cls_name = pinyin.get_pinyin(cls_name)
            print('该类特征数为{}'.format(len(samples_cls)))
            # 开始遍历一个类别
            hist_per_cls = []

            height = 500
            repeat_times = int(height/len(samples_cls))
            for idx2, sample in enumerate(samples_cls):
                hist = sample['hist']
                cls = sample['cls']
                self.get_single_hist_info(hist=hist)
                hist = self.get_single_fmap(cls=cls, hist=hist,fmap_type='1dim')
                if idx2 == len(samples_cls) - 1:
                    repeat_times = height - idx2*repeat_times
                for _ in range(repeat_times):
                    hist_per_cls.append(hist)


            hist_per_cls = np.array(hist_per_cls)
            plt.subplot(5,4,idx+1)
            all_hist += hist_per_cls
            plt.imshow(hist_per_cls)
            plt.title('The cls is {}'.format(cls_name))

        plt.show()

    def __repr__(self):
        return '可视化特征库特征 beta v1'


if __name__ == '__main__':
    db = Database()
    db.connect_db()
    samples = db.get_samples()
    visualizer = VisHist(samples=samples)
    # visualizer.get_single_hist_info(samples[0]['hist'])
    visualizer.get_fmap_per_cls()
