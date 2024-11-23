import os.path
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from datetime import datetime

from keras.src.utils import save_img

from generate_denoise_image import generate_denoise_image
from utils import utils_image as util


class ProcessingSection(tk.Frame):
    def __init__(self, root):
        self.uploaded_image = None
        self.height = 606
        self.width = 830
        self.bg = "#000000"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        image_section = tk.Frame(self, bg="#26282A", height=500, width=810)
        image_section.grid_propagate(False)
        image_section.grid(row=0, column=0, padx=10, pady=10)
        image_section.grid_rowconfigure(0, weight=1)
        image_section.grid_columnconfigure(0, weight=1)

        self.add_icon = Image.open("assets/circle-plus-white.png")
        self.add_icon = ImageTk.PhotoImage(self.add_icon)
        add_icon_label = tk.Label(image_section, image=self.add_icon, bg="#26282A")
        add_icon_label.grid(row=0, column=0, sticky="nsew")

        image_section.bind("<Enter>", lambda e: (
            image_section.config(bg="#33363A"),
            add_icon_label.config(bg="#33363A"),
            add_icon_label.config(bg="#33363A")
        ))
        image_section.bind("<Leave>", lambda e: (
            image_section.config(bg="#26282A"),
            add_icon_label.config(bg="#26282A"),
            add_icon_label.config(bg="#26282A")
        ))
        add_icon_label.bind("<Button-1>", lambda e: (
            self.upload_image()
        ))

        # 인터페이스 섹션
        self.interface_Section = tk.Frame(self, bg="#26282A", height=76, width=810)
        self.interface_Section.grid_propagate(False)
        self.interface_Section.grid(row=1, column=0, padx=10)

        convert_button_img = Image.open("assets/convert_btn.png").resize((140, 40))
        convert_button_img = ImageTk.PhotoImage(convert_button_img)
        self.convert_btn = tk.Button(self.interface_Section, image=convert_button_img)
        self.convert_btn.grid(row=0, column=0, sticky="nsew")

    def upload_image(self):
        file_path = tk.filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")],
        )
        if file_path:
            self.uploaded_image = Image.open(file_path)
            self.save_img(file_path, self.uploaded_image)

            max_len = 400
            x, y = self.uploaded_image.size

            self.uploaded_image = self.uploaded_image.resize((max_len,int(max_len * y / x)) if x > y else (int(max_len * x / y), max_len))


            self.uploaded_image = ImageTk.PhotoImage(self.uploaded_image)

            image_label = tk.Label(self, image=self.uploaded_image)
            image_label.grid(row=0, column=0)

            # test
            img_name, ext = os.path.splitext(os.path.basename(file_path))
            util.imsave(generate_denoise_image(file_path), f'image/result/{img_name}_denoised.{ext}')

    def save_img(self, path, img):
        type = path.split(".")[-1]
        img.save(f"image/original/{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.{type}")

        # # 이미지 로드
        # self.before_image = Image.open("image/img1.jpg")
        # img_w = self.before_image.width
        # img_h = self.before_image.height
        # ratio = img_w / img_h
        #
        # self.before_image = self.before_image.resize((810, int(810 / ratio)))
        # self.before_image = ImageTk.PhotoImage(self.before_image)
        #
        # self.after_image = Image.open("image/img2.jpg")
        # self.after_image = ImageTk.PhotoImage(self.after_image)
        #
        # self.image_label = tk.Label(self, image=self.before_image)
