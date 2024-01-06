import os
import random
from tqdm import tqdm
import shutil

def split_dataset(data_root, train_ratio=0.7):
    categories = [name for name in os.listdir(data_root) if os.path.isdir(os.path.join(data_root, name))]

    for category in categories:
        category_path = os.path.join(data_root, category)
        images = [name for name in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, name))]
        random.shuffle(images)

        split_index = int(len(images) * train_ratio)

        train_path = os.path.join(data_root, 'train', category)
        val_path = os.path.join(data_root, 'val', category)
        os.makedirs(train_path, exist_ok=True)
        os.makedirs(val_path, exist_ok=True)

        for i, image in enumerate(tqdm(images, desc=f"Processing {category}")):
            src_path = os.path.join(category_path, image)
            if i < split_index:
                dst_path = os.path.join(train_path, image)
            else:
                dst_path = os.path.join(val_path, image)
            shutil.copy(src_path, dst_path)

    print("数据集划分完成，训练集和验证集已保存在 'train' 和 'val' 文件夹中。")

# 使用示例
data_root_path = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/oxbuild_images_splits'  # 修改为你的数据集路径
split_dataset(data_root_path)
