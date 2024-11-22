import tkinter as tk
from PIL import Image, ImageTk

class Navbar(tk.Frame):
    def __init__(self, root, switch_section_callback):
        self.height = 606
        self.width = 250
        self.bg = "#26282A"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        self.switch_section_callback = switch_section_callback

        self.rowconfigure(40, weight=1)

        self.initUI()

    def initUI(self):
        self.setLogo(5, 0)

        self.setSeparator(9, 0, 250, 1)

        self.houseIcon = Image.open("./assets/house-white.png")
        self.houseIcon = ImageTk.PhotoImage(self.houseIcon)
        self.setMenu(15, 0, self.houseIcon, "Home", lambda: self.switch_section_callback("Processing"))

        self.listIcon = Image.open("./assets/list-white.png")
        self.listIcon = ImageTk.PhotoImage(self.listIcon)
        self.setMenu(25, 0, self.listIcon, "History", lambda: self.switch_section_callback("History"))

        self.setSeparator(41, 0, 250, 1)

        self.setFooter(45, 0)

    def setLogo(self, row, column):
        logo = tk.Label(self, text="Memory Mender", fg="white", bg=self.bg, font=("Helvetica, 24"))
        logo.grid(row=row, column=column, sticky="w", padx=20, pady=20)

    def setSeparator(self, row, column, width, height):
        separator = tk.Frame(self, bg="#ffffff", width=width, height=height)
        separator.grid(row=row, column=column)

    def setMenu(self, row, column, icon, text, command):
        menuFrame = tk.Frame(self, bg=self.bg, height=60, width=250)
        menuFrame.grid_propagate(False)
        menuFrame.grid(row=row, column=column)
        menuFrame.grid_rowconfigure(0, weight=1)

        icon_label = tk.Label(menuFrame, image=icon, bg=self.bg)
        icon_label.grid(row=0, column=0, padx=20, sticky="w")

        text_label = tk.Label(menuFrame, text=text, fg="white", bg=self.bg, font=("Helvetica, 16"))
        text_label.grid(row=0, column=1, sticky="w")

        menuFrame.bind("<Enter>", lambda e: (menuFrame.config(bg="#33363A"), icon_label.config(bg="#33363A"), text_label.config(bg="#33363A")))
        menuFrame.bind("<Leave>", lambda e: (menuFrame.config(bg=self.bg), icon_label.config(bg=self.bg), text_label.config(bg=self.bg)))
        menuFrame.bind("<Button-1>", lambda e: command())

    def setFooter(self, row, column):
        footer = tk.Label(self, text="© 2021 Memory Mender", fg="white", bg=self.bg, font=("Helvetica, 10"))
        footer.grid(row=row, column=column, sticky="s", padx=20, pady=20)