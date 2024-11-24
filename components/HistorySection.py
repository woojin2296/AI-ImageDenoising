import tkinter as tk
import os
from PIL import Image, ImageTk

class HistorySection(tk.Frame):
    def __init__(self, root):
        self.height = 606
        self.width = 830
        self.bg = "#000000"

        self.title_section_height = 40
        self.title_section_width = self.width - 20
        self.title_section_bg = self.bg

        self.card_height = 200
        self.card_width = 250
        self.card_bg = "#26282A"

        self.page = 0
        self.image_path = []
        self.images = dict()

        self.load_img()

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0, ipadx=20)

        self.title_section().grid(row=0, column=0, columnspan=3, padx=10)
        self.setPage()

    def title_section(self):
        title_section = tk.Frame(self, bg=self.title_section_bg, height=self.title_section_height, width=self.title_section_width)
        title_section.grid_propagate(False)
        title_section.grid_rowconfigure(0, weight=1)
        title_section.grid_columnconfigure(0, weight=1)

        title_label = tk.Label(title_section, text="History", fg="white", bg=self.title_section_bg, font=("Helvetica, 18"))
        title_label.grid(row=0, column=0, sticky="nsw")

        return title_section

    def load_img(self):
        self.image_path = os.listdir("image/result")

        for path in self.image_path:
            name = path.split(".")[0]

            original_image = Image.open("image/original/" + path)
            result_image = Image.open("image/result/" + path)

            original_image = self.__resize_image(original_image)
            result_image = self.__resize_image(result_image)

            original_image = ImageTk.PhotoImage(original_image)
            result_image = ImageTk.PhotoImage(result_image)
            self.images[name] = [original_image, result_image]

    def setPage(self):
        for index, path in enumerate(self.image_path):
            self.setHistoryCard(index, path)

    def __resize_image(self, image: Image):
        x, y = image.size

        if x > y:
            image = image.resize(((250-4), int((250-4) * y / x)))
        else:
            image = image.resize((int((self.card_height-44) * x / y), (self.card_height-44)))

        return image

    def setHistoryCard(self, index, path):
        card = tk.Frame(self, width=250, height=200, bg="#26282A")
        card.grid_propagate(False)
        card.grid_columnconfigure(0, weight=1)
        card.grid_rowconfigure(0, weight=1)
        card.grid(row=index // 3 + 1, column=index % 3, padx=10, pady=10)

        path = path.split(".")[0]
        original_image = self.images[path][0]

        image_label = tk.Label(card, image=original_image, bg="#26282A")
        image_label.grid(row=0, column=0)

        name_label = tk.Label(card, text=path, fg="white", bg="#26282A", font=("Helvetica, 16"))
        name_label.grid(row=2, column=0, padx=10, pady=10, sticky="s")

        image_label.bind("<Enter>", lambda e: (
            image_label.config(image=self.images[path][1]),
        ))
        image_label.bind("<Leave>", lambda e: (
            image_label.config(image=self.images[path][0]),
        ))



