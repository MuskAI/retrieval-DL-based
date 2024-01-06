#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：retrieval-DL-based 
@File    ：simple_vis.py
@IDE     ：PyCharm 
@Author  ：haoran
@Date    ：2024/1/5 22:00

利用matplotlib对返回的result进行显示，有一个参数k控制显示的数量
'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：retrieval-DL-based 
@File    ：visualize.py
@IDE     ：PyCharm 
@Author  ：haoran
@Date    ：2024/1/5 20:36

对检索的结果进行显示

'''
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog  # 引入文件对话框模块

class ImageDisplayApp:
    def __init__(self, root, result, k=5):
        self.root = root
        self.result = result
        self.k = k
        self.current_index = 0

        self.image_labels = []
        self.cls_labels = []
        self.dis_labels = []

        self.create_widgets()
        self.show_images()

        # 添加按钮用于选择图片路径并显示在第一个位置上
        self.add_button()

    def create_widgets(self):
        # 主要的Frame，包含图像和标签
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(expand=True, fill="both")

        # 计算行数和列数以调整布局
        rows = (self.k + 2) // 3
        cols = 3

        for i in range(rows):
            self.main_frame.grid_rowconfigure(i, weight=1)  # 添加行权重以支持垂直居中
            self.main_frame.grid_columnconfigure(i, weight=1)  # 添加列权重以支持水平居中

        for i in range(self.k):
            frame = tk.Frame(self.main_frame, padx=10, pady=10)
            frame.grid(row=i // cols, column=i % cols, sticky='nsew')  # 使用sticky参数进行居中对齐

            img_label = tk.Label(frame)
            img_label.pack()

            self.image_labels.append(img_label)

            cls_label = tk.Label(frame, text="cls:", font=("Arial", 14))  # 修改字体大小为14
            cls_label.pack(anchor='w')
            self.cls_labels.append(cls_label)

            dis_label = tk.Label(frame, text="dis:", font=("Arial", 14))  # 修改字体大小为14
            dis_label.pack(anchor='w')
            self.dis_labels.append(dis_label)

    def show_images(self):
        for i in range(self.k):
            if self.current_index < len(self.result):
                img_path = self.result[self.current_index]['img']
                img = Image.open(img_path)
                img = img.resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)

                self.image_labels[i].config(image=photo)
                self.image_labels[i].image = photo

                cls = self.result[self.current_index]['cls']
                dis = "{:.5f}".format(self.result[self.current_index]['dis'])  # 保留小数点后5位

                self.cls_labels[i].config(text="cls: " + cls)
                self.dis_labels[i].config(text="dis: " + dis)

                self.current_index += 1
            else:
                break

    def add_button(self):
        # 创建按钮并绑定函数
        btn = tk.Button(self.root, text="选择图片", command=self.select_image)
        btn.pack(side="bottom", fill="x")  # 放置在整个界面底部

    def select_image(self):
        # 通过文件对话框选择图片路径
        file_path = filedialog.askopenfilename(title="选择图片")
        if file_path:
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)

            self.image_labels[0].config(image=photo)
            self.image_labels[0].image = photo

if __name__ == "__main__":

    project_root = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/retrieval-DL-based/image_retrieval'

    result = [{'cls': 'all', 'dis': 1.1920928955078125e-07,
               'img': project_root + '/database/all/all_souls_000001-md5-23d1df9a8a3874b5e20503c23463aa57.jpg'},
              # 其他图像数据...
              {'cls': 'new', 'dis': 0.18739688396453857,
               'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'},
              {'cls': 'new', 'dis': 0.18739688396453857,
               'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'},
              {'cls': 'new', 'dis': 0.18739688396453857,
               'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'},
              {'cls': 'new', 'dis': 0.18739688396453857,
               'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'},
              {'cls': 'new', 'dis': 0.18739688396453857,
               'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'},
              {'cls': 'new', 'dis': 0.18739688396453857,
               'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'}]


    k = 8  # 设置要显示的图片数量

    root = tk.Tk()
    app = ImageDisplayApp(root, result, k)
    root.mainloop()
