import tkinter as tk
import os
from PIL import Image, ImageTk

class HistorySection(tk.Frame):
    def __init__(self, root):
        self.height = 606
        self.width = 830
        self.bg = "#000000"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0, ipadx=20)

        self.page = 0
        self.images = []
        self.load_img()

        self.setPage()

    def load_img(self):
        original_images = os.listdir("image/original")
        result_images = os.listdir("image/result")

        for original, result in zip(original_images, result_images):
            original_image = Image.open("image/original/" + original)
            original_image = ImageTk.PhotoImage(original_image)
            result_image = Image.open("image/result/" + result)
            result_image = ImageTk.PhotoImage(result_image)

            self.images.append((original_image, result_image))

    def setPage(self):
        for i in range(len(self.images)):
            self.setHistoryCard(i)


    def setHistoryCard(self, index):
        card = tk.Frame(self, width=250, height=200, bg="#26282A")
        card.grid(row=index // 3, column=index % 3, padx=10, pady=10)

