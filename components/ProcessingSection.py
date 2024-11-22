import tkinter as tk
from PIL import Image, ImageTk

class ProcessingSection(tk.Frame):
    def __init__(self, root):
        self.height = 606
        self.width = 830
        self.bg = "#000000"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        # 이미지 로드
        self.before_image = Image.open("image/img1.jpg")

        img_w = self.before_image.width
        img_h = self.before_image.height
        ratio = img_w / img_h

        self.before_image = self.before_image.resize((810, int(810 / ratio)))
        self.before_image = ImageTk.PhotoImage(self.before_image)

        self.after_image = Image.open("image/img2.jpg")
        self.after_image = ImageTk.PhotoImage(self.after_image)

        self.image_label = tk.Label(self, image=self.before_image)

        # 이미지 섹션
        self.image_Section = tk.Frame(self, bg="#26282A", height=500, width=810)
        self.image_Section.grid(row=0, column=0, padx=10, pady=10)

        # 인터페이스 섹션
        self.interface_Section = tk.Frame(self, bg="#26282A", height=76, width=810)
        self.interface_Section.grid(row=1, column=0, padx=10)
