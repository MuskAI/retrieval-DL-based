# -*- coding: utf-8 -*-
# __version__= demo_beta_v_2_0
# __author__ = haolin & haoran
# 该版本是在1.0的基础上增加了增量学习的功能，在csv表项中增加了md5项
from __future__ import print_function

import pandas as pd
import os
from hashlib import md5
import time
import re


class Database(object):

    def __init__(self,DB_dir='../database',DB_csv='../data.csv'):
        self.DB_dir = DB_dir
        self.DB_csv = DB_csv

        self._gen_csv()
        self.data = pd.read_csv(DB_csv)
        self.classes = set(self.data["cls"])

    def _gen_csv(self):
        if os.path.exists(self.DB_csv):
            return
        with open(self.DB_csv, 'w', encoding='UTF-8') as f:
            f.write("img,cls,md5,blacklists")
            for root, _, files in os.walk(self.DB_dir, topdown=False):
                cls = root.split('/')[-1]
                for name in files:
                    if not name.endswith('.png') and not name.endswith('.jpg'):
                        continue
                    img = os.path.join(root, name)
                    if 'md5' in name:
                        # 如果编码已经在文件名中，则可以直接从图片名称中获得编码
                        f.write("\n{},{},{},{}".format(img, cls, name.split('-')[-1].split('.')[0], 0))
                    else:
                        # 如果编码没有在文件名中，则进行编码并修改文件名
                        md5_code = self.get_md5(img_path=img)
                        os.rename(img, os.path.join(root, '{}-md5-{}.{}'.format(name.split('.')[0],
                                                                                md5_code,
                                                                                name.split('.')[-1])))

                        f.write("\n{},{},{},{}".format(img, cls, md5_code, 0))

    def __len__(self):
        return len(self.data)

    def get_class(self):
        return self.classes

    def get_data(self):
        return self.data

    def get_md5(self, img_path):
        """
        对图片进行md5编码，编码成功则返回str，失败则返回None
        Args:
            img_path: [str] 需要编码图片的地址

        """
        assert os.path.isfile(img_path)

        try:
            with open(img_path, 'rb') as img:
                md5_code = md5(img.read()).hexdigest()
        except Exception as e:
            return None

        return md5_code


if __name__ == "__main__":
    start = time.time()
    db = Database()
    data = db.get_data()
    classes = db.get_class()

    print("DB length:", len(db))
    print(classes)
    print('Construct Database :{:.5f}'.format(time.time() - start))
