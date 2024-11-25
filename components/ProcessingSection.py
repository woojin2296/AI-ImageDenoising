import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from datetime import datetime

from generate_denoise_image import generate_denoise_image

class ProcessingSection(tk.Frame):
    def __init__(self, root):
        self.height = 606
        self.width = 830
        self.bg = "#000000"

        self.title_section_height = 40
        self.title_section_width = self.width - 20
        self.title_section_bg = self.bg

        self.image_section_height = 470
        self.image_section_width = self.width - 20
        self.image_section_bg = "#26282A"
        self.image_section_bg_hover = "#33363A"

        self.interface_Section_height = 76
        self.interface_Section_width = self.width - 20
        self.interface_Section_bg = "#26282A"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        self.initUI()

    def initUI(self):
        self.title_section().grid(row=0, column=0, padx=10)
        self.image_section().grid(row=1, column=0, padx=10)
        self.padding_section().grid(row=2, column=0)
        self.interface_section().grid(row=3, column=0, padx=10)

    def padding_section(self):
        return tk.Frame(self, bg=self.bg, height=10, width=self.width)

    def title_section(self):
        title_section = tk.Frame(self, bg=self.title_section_bg, height=self.title_section_height, width=self.title_section_width)
        title_section.grid_propagate(False)
        title_section.grid_rowconfigure(0, weight=1)
        title_section.grid_columnconfigure(0, weight=1)

        title_label = tk.Label(title_section, text="Upload Image", fg="white", bg=self.title_section_bg, font=("Helvetica, 18"))
        title_label.grid(row=0, column=0, sticky="nsw")

        return title_section

    def image_section(self):
        image_section = tk.Frame(self, bg=self.image_section_bg, height=self.image_section_height, width=self.image_section_width)
        image_section.grid_propagate(False)
        image_section.grid_rowconfigure(0, weight=1)
        image_section.grid_columnconfigure(0, weight=1)

        self.add_icon = Image.open("assets/circle-plus-white.png")
        self.add_icon = ImageTk.PhotoImage(self.add_icon)

        self.image_placeholder = tk.Label(image_section, image=self.add_icon, bg=self.image_section_bg)
        self.image_placeholder.grid(row=0, column=0, sticky="nsew")

        self.image_placeholder.bind("<Enter>", lambda e: self.image_placeholder.config(bg=self.image_section_bg_hover))
        self.image_placeholder.bind("<Leave>", lambda e: self.image_placeholder.config(bg=self.image_section_bg))
        self.image_placeholder.bind("<Button-1>", lambda e: self.upload_image())

        return image_section

    def upload_image(self):
        self.file_path = tk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

        if self.file_path:
            self.original_image = Image.open(self.file_path)
            self.img_name = f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.{self.file_path.split(".")[-1]}'

            self.display_image = self.__resize_image(self.original_image)
            self.display_image = ImageTk.PhotoImage(self.display_image)
            self.image_placeholder.config(image=self.display_image)

    def __resize_image(self, image: Image):
        x, y = image.size
        if x < y:
            image = image.resize((self.image_section_width, int(self.image_section_width * y / x)))
        else:
            image = image.resize((int(self.image_section_height * x / y), self.image_section_height))
        return image

    def interface_section(self):
        self.interface_Section = tk.Frame(self, bg=self.interface_Section_bg, height=self.interface_Section_height, width=self.interface_Section_width)
        self.interface_Section.grid_propagate(False)
        self.interface_Section.grid(row=2, column=0, padx=10)
        self.interface_Section.grid_rowconfigure(0, weight=1)

        convert_button_img = Image.open("assets/convert_btn.png").resize((140, 40))
        convert_button_img = ImageTk.PhotoImage(image=convert_button_img)
        convert_btn = tk.Label(self.interface_Section, image=convert_button_img, bg="#26282A")
        convert_btn.image = convert_button_img
        convert_btn.grid(row=0, column=0, sticky="nsew")

        download_button_img = Image.open("assets/download_btn.png").resize((140, 40))
        download_button_img = ImageTk.PhotoImage(image=download_button_img)
        download_btn = tk.Label(self.interface_Section, image=download_button_img, bg="#26282A")
        download_btn.image = download_button_img
        download_btn.grid(row=0, column=1, sticky="nsew")

        convert_btn.bind("<Button-1>", lambda e: (
            self.__convert_button_pressed()
        ))

        download_btn.bind("<Button-1>", lambda e: (
            self.__download_button_pressed()
        ))

        return self.interface_Section

    def __convert_button_pressed(self):
        self.converted_image = Image.fromarray(generate_denoise_image(self.file_path))

        self.original_image.save(f'image/original/{self.img_name}')
        self.converted_image.save(f'image/result/{self.img_name}')

        self.converted_image_rescale = self.__resize_image(self.converted_image)
        self.converted_image_rescale = ImageTk.PhotoImage(self.converted_image_rescale)
        self.image_placeholder.config(image=self.converted_image_rescale)

    def __download_button_pressed(self):
        save_path = tk.filedialog.asksaveasfilename(initialfile=self.img_name, filetypes=[("Image files", "*.jpg *.jpeg *.png")], defaultextension=".png", initialdir="downloads")
        if save_path:
            self.converted_image.save(save_path)