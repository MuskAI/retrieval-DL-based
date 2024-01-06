"""
@author:haoran in deeptk
version:beta 1.0
实现根据图片删除数据库中易混淆特征的功能：
1. 读取图片，进行单图推理得到该图特征
2. 计算距离，距离最相似的第一个为待删除的特征
3. 从文件目录中删除该图
"""
import os

from apis.dataproc_md5 import Database
from model_zoo.mobilenet_v2_md5 import MobileNetV2Feat
from apis.infer import infer
from main import inference



class Removal:
    def __init__(self,img):
        self.db = Database()
        self.img = img
    def del_confusion_image(self):
        method = MobileNetV2Feat()
        method.__init__(cache_dir='../cache',model_path='../model_zoo/checkpoint/ret_mobilenet_v2.onnx')
        samples = method.make_samples(self.db)
        query = method.make_single_sample(self.img)
        print('img to be tested:', query)
        # parameters
        topd = 1
        topk = 1
        d_type = 'd1'  # distance type  you can choose 'd1 , d2 , d3  ... d8' and 'cosine' and 'square'
        top_cls, result, std_result = infer(query, samples=samples,depth=topd, d_type=d_type, topk=topk)
        print('topk possible predicted classes:', top_cls)
        print('topd nearest distance matching from the database:', result)

        # 根据md5码找到图片
        data = self.db.get_data()
        csv_md5_list = list(data['md5'])

        # 找到编码对应的图片地址
        need_del = data.loc[csv_md5_list.index(result[0]['md5'])]

        # 开始删除对应图片和csv文件
        print('删除的图片地址:{}\n删除的图片类别:{}'.format(need_del['img'],need_del['cls']))

        try:
            os.remove(path=need_del['img'])
            print('删除成功')
            os.remove('../data.csv')
        except Exception as e:
            print('删除图片失败')



if __name__ == '__main__':
    img = '../test.png'
    remover = Removal(img=img)
    remover.del_confusion_image()




