import tkinter as tk
from PIL import Image, ImageTk

class Navbar(tk.Frame):
    def __init__(self, root, switch_section_callback):

        self.config = {
            "height": 606,
            "width": 250,
            "bg": "#26282A",
            "menu_hover_bg": "#33363A",
            "separator_color": "#ffffff",
            "text_color": "#ffffff"
        }

        tk.Frame.__init__(self, root, bg=self.config["bg"], height=self.config["height"], width=self.config["width"])
        self.grid_propagate(False)
        self.grid(row=0, column=0)
        self.rowconfigure(40, weight=1)

        self.switch_section_callback = switch_section_callback

        self.icons = {}
        self.load_icons()

        self.initUI()

    def load_icons(self):
        self.icons["house"] = ImageTk.PhotoImage(Image.open("./assets/house-white.png"))
        self.icons["list"] = ImageTk.PhotoImage(Image.open("./assets/list-white.png"))

    def initUI(self):
        self.logo("Memory Mender").grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.separator().grid(row=1, column=0)

        self.set_menu(
            row=15,
            column=0,
            icon=self.icons["house"],
            text="Home",
            command=lambda: self.switch_section_callback("Processing")
        )
        self.set_menu(
            row=25,
            column=0,
            icon=self.icons["list"],
            text="History",
            command=lambda: self.switch_section_callback("History")
        )

        self.separator().grid(row=41, column=0)
        self.set_footer("© 2024 Memory Mender", row=45, column=0)

    def logo(self, text):
        return tk.Label(
            self,
            text=text,
            fg=self.config["text_color"],
            bg=self.config["bg"],
            font=("Helvetica, 24")
        )
    def separator(self):
        return tk.Frame(
            self,
            bg=self.config["separator_color"],
            width=self.config["width"],
            height=1
        )

    def set_menu(self, row, column, icon, text, command):
        menu_frame = self.create_menu_frame(row, column)
        icon_label, text_label = self.create_menu_content(menu_frame, icon, text)

        self.bind_menu_interaction(menu_frame, icon_label, text_label, command)

    def create_menu_frame(self, row, column):
        menu_frame = tk.Frame(
            self,
            bg=self.config["bg"],
            height=60,
            width=self.config["width"]
        )
        menu_frame.grid_propagate(False)
        menu_frame.grid(row=row, column=column)
        menu_frame.grid_rowconfigure(0, weight=1)
        return menu_frame

    def create_menu_content(self, menu_frame, icon, text):
        icon_label = tk.Label(menu_frame, image=icon, bg=self.config["bg"])
        icon_label.grid(row=0, column=0, padx=20, sticky="w")

        text_label = tk.Label(
            menu_frame,
            text=text,
            fg=self.config["text_color"],
            bg=self.config["bg"],
            font=("Helvetica, 16")
        )
        text_label.grid(row=0, column=1, sticky="w")
        return icon_label, text_label

    def bind_menu_interaction(self, menu_frame, icon_label, text_label, command):
        menu_frame.bind(
            "<Enter>",
            lambda e: self.change_menu_color(menu_frame, icon_label, text_label, self.config["menu_hover_bg"])
        )
        menu_frame.bind(
            "<Leave>",
            lambda e: self.change_menu_color(menu_frame, icon_label, text_label, self.config["bg"])
        )

        for widget in [menu_frame, icon_label, text_label]:
            widget.bind("<Button-1>", lambda e: command())

    def change_menu_color(self, menu_frame, icon_label, text_label, color):
        menu_frame.config(bg=color)
        icon_label.config(bg=color)
        text_label.config(bg=color)

    def set_footer(self, text, row, column):
        footer = tk.Label(
            self,
            text=text,
            fg=self.config["text_color"],
            bg=self.config["bg"],
            font=("Helvetica, 10")
        )
        footer.grid(row=row, column=column, sticky="s", padx=20, pady=20)