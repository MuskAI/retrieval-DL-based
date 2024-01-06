import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class ImageDisplayApp:
    def __init__(self, root):
        self.root = root
        self.result = []
        self.k = 0
        self.current_index = 0

        self.preview_label = tk.Label(self.root)
        self.preview_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.select_button = tk.Button(self.root, text="选择图片", command=self.select_image)
        self.select_button.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # self.retrieval_button = tk.Button(self.root, text="开始检索", command=self.start_retrieval)
        # self.retrieval_button.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

        self.image_labels = []
        self.cls_labels = []
        self.dis_labels = []

        for i in range(8):

            img_label = tk.Label(self.root)
            img_label.grid(row=i // 4 + 3, column=i % 4, padx=15, pady=15)
            self.image_labels.append(img_label)

            cls_label = tk.Label(self.root, font=("Arial", 12))
            cls_label.grid(row=i // 4 + 4, column=i % 4, sticky='w')
            self.cls_labels.append(cls_label)

            dis_label = tk.Label(self.root, font=("Arial", 12))
            dis_label.grid(row=i // 4 + 5, column=i % 4, sticky='w')
            self.dis_labels.append(dis_label)
    #
    def select_image(self):
        file_path = filedialog.askopenfilename(title="选择图片")
        if file_path:
            img = Image.open(file_path)
            img = img.resize((200, 200), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.preview_label.config(image=img)
            self.preview_label.image = img  # 保存图片的引用
        return file_path

    # def start_retrieval(self):
    #     # 模拟检索算法返回的result
    #     # 请用实际的检索算法替换这部分内容
    #     project_root = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/retrieval-DL-based/image_retrieval'
    #
    #     self.result = [{'cls': 'all', 'dis': 1.1920928955078125e-07,
    #                     'img': project_root + '/database/all/all_souls_000001-md5-23d1df9a8a3874b5e20503c23463aa57.jpg'},
    #                    # 其他图像数据...
    #                    {'cls': 'new', 'dis': 0.18739688396453857,
    #                     'img': project_root + '/database/new/new_000294-md5-04ff21484825541d05c0c50346e35f49.jpg'},
    #                    {'cls': 'all', 'dis': 1.1920928955078125e-07,
    #                     'img': project_root + '/database/all/all_souls_000001-md5-23d1df9a8a3874b5e20503c23463aa57.jpg'}
    #                    ]
    #
    #     self.k = min(3, len(self.result))  # 设置要显示的图片数量
    #
    #
    #
    #     self.show_images()
    def show_result(self,result):
        # 模拟检索算法返回的result
        # 请用实际的检索算法替换这部分内容

        self.result = result
        self.k = min(3, len(self.result))  # 设置要显示的图片数量

        self.show_images()
    def show_images(self):
        for i in range(self.k):
            if self.current_index < len(self.result):
                img_path = self.result[self.current_index]['img']
                # project_root = '/Users/musk/Desktop/一箪食一壶浆/闲鱼接单/图像检索/retrieval-DL-based/image_retrieval'
                img = Image.open(img_path)
                img = img.resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(img)

                self.image_labels[i].config(image=photo)
                self.image_labels[i].image = photo

                cls = self.result[self.current_index]['cls']
                dis = "{:.5f}".format(self.result[self.current_index]['dis'])  # 保留小数点后5位

                self.cls_labels[i].config(text="类别: " + cls)
                self.dis_labels[i].config(text="特征距离: " + dis)

                self.current_index += 1
            else:
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDisplayApp(root)
    root.mainloop()
