import numpy as np
import onnx.utils
import onnxruntime as ort
import cv2
import os,sys
import tqdm
from six.moves import cPickle
sys.path.append('../model_zoo/')
sys.path.append('./model_zoo/')


import matplotlib.pyplot as plt
from hashlib import md5
class FeatExtractor(object):
    def __init__(self, cache_dir='cache', model_path=''):
        """

        @param cache_dir:
        @param model_path:
        @param detector_model_path: 目标检测模型的路径
        @param autocrop: 是否使用目标检测模型进行AI Crop
        """
        self.cache_dir = cache_dir
        self.model_path = model_path
        self.image_size = (224,224)
        # 判断模型存在情况
        if not os.path.isfile(model_path):
            raise '检索模型不存在'


        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def make_single_sample(self, d_img, verbose=True,md5_encoding=True):
        # crop_range_ratio = (0.2,0.8)
        res_model = ort.InferenceSession(self.model_path)
        input_name = res_model.get_inputs()[0].name
        output_name = res_model.get_outputs()[0].name
        result = None
        if verbose:
            print("Start to use Model to generate features for DataBase")
        if md5_encoding:
            md5_code = self.get_md5(img_path=d_img)

        # 读取图片
        # transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))

        img = cv2.imread(d_img)

        img = img.astype(np.float32)

        mean = np.array([0.4914, 0.4822, 0.4465])*255
        std = np.array([0.2023, 0.1994, 0.2010])*255
        mean = np.float64(mean.reshape(1, -1))
        stdinv = 1 / np.float64(std.reshape(1, -1))
        cv2.subtract(img, mean, img)  # inplace
        cv2.multiply(img, stdinv, img)  # inplace
        img = cv2.resize(img, self.image_size)
        img = np.array([img])
        img = np.transpose(img, [0, 3, 1, 2])
        output = res_model.run([output_name], {input_name: img})
        d_hist = output[0][0]
        # d_hist /= np.sum(d_hist)
        result = {
            'img': d_img,
            'cls': 'unknown',
            'hist': d_hist,
            'md5': md5_code if md5_encoding else 'unknown',
        }
        return result


    def get_md5(self, img_path):
        """
        对图片进行md5编码，编码成功则返回str，失败则返回None
        Args:
            img_path: [str] 需要编码图片的地址

        """
        # assert os.path.isfile(img_path)

        try:
            with open(img_path, 'rb') as img:
                md5_code = md5(img.read()).hexdigest()
        except Exception as e:
            return None

        return md5_code

class OxfordFeatExtractor(object):
    def __init__(self, cache_dir='cache', model_path=''):
        """

        @param cache_dir:
        @param model_path:
        @param detector_model_path: 目标检测模型的路径
        @param autocrop: 是否使用目标检测模型进行AI Crop
        """
        self.cache_dir = cache_dir
        self.model_path = model_path
        self.image_size = (224,224)
        # 判断模型存在情况
        if not os.path.isfile(model_path):
            raise '检索模型不存在'

        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def make_single_sample(self, d_img, verbose=True,md5_encoding=True):
        # crop_range_ratio = (0.2,0.8)
        res_model = ort.InferenceSession(self.model_path)
        input_name = res_model.get_inputs()[0].name
        output_name = res_model.get_outputs()[0].name
        result = None
        if verbose:
            print("Start to use Big Model to generate features for DataBase")
        if md5_encoding:
            md5_code = self.get_md5(img_path=d_img)

        # 读取图片
        # transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
        img = cv2.imread(d_img)
        img = img.astype(np.float32)

        mean = np.array([0.4914, 0.4822, 0.4465])*255
        std = np.array([0.2023, 0.1994, 0.2010])*255
        mean = np.float64(mean.reshape(1, -1))
        stdinv = 1 / np.float64(std.reshape(1, -1))
        cv2.subtract(img, mean, img)  # inplace
        cv2.multiply(img, stdinv, img)  # inplace
        img = cv2.resize(img, self.image_size)
        img = np.array([img])
        img = np.transpose(img, [0, 3, 1, 2])
        output = res_model.run([output_name], {input_name: img})
        d_hist = output[0][0]
        # d_hist /= np.sum(d_hist)
        result = {
            'img': d_img,
            'cls': 'unknown',
            'hist': d_hist,
            'md5': md5_code if md5_encoding else 'unknown',
        }
        return result


    def get_md5(self, img_path):
        """
        对图片进行md5编码，编码成功则返回str，失败则返回None
        Args:
            img_path: [str] 需要编码图片的地址

        """
        # assert os.path.isfile(img_path)

        try:
            with open(img_path, 'rb') as img:
                md5_code = md5(img.read()).hexdigest()
        except Exception as e:
            return None

        return md5_code

