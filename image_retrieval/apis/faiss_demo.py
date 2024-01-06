#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：shengxian_retrieval_onnx 
@File    ：faiss_demo.py
@IDE     ：PyCharm 
@Author  ：haoran
@Date    ：2022/4/25 17:19 
'''
import numpy as np
import time
import faiss





if __name__ == '__main__':
    d = 1280  # dimension
    nb = 50000  # database size
    nq = 1  # nb of queries
    np.random.seed(1234)  # make reproducible
    xb = np.random.random((nb, d)).astype('float32')
    xb_len = np.linalg.norm(xb, axis=1, keepdims=True)
    xb = xb / xb_len
    xq = np.random.random((nq, d)).astype('float32')
    xq_len = np.linalg.norm(xq, axis=1, keepdims=True)
    xq = xq / xq_len
    # CPU

    t1 = time.time()
    # index = faiss.IndexFlat(d, faiss.METRIC_INNER_PRODUCT)  # 建立索引
    index = faiss.IndexFlatIP(d)
    # 或者通过faiss.indexFlatIP(内积)实现
    index.add(xb)  # add vectors to the index
    nlist = 1 # we want to see 4 nearest neighbors
    for i in range(10):
        D, I = index.search(-xq, nlist)  # actual search
    t2 = time.time()
    print(D[0] + [1 for i in range(len(D[0]))],I)
    # print(D[0],I)

    print('faiss spend time %.4f' % ((t2 - t1) / 10))

