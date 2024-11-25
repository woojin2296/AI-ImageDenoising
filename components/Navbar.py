import tkinter as tk
from PIL import Image, ImageTk

class Navbar(tk.Frame):
    def __init__(self, root, switch_section_callback):

        self.icons = {}
        self.switch_section_callback = switch_section_callback
        self.config = {
            "height": 606,
            "width": 250,
            "bg": "#26282A",

            "text_color": "#ffffff",

            "menu_height": 60,
            "menu_hover_bg": "#33363A",

            "separator_height": 1,
            "separator_color": "#ffffff",
        }

        self.load_icons()

        tk.Frame.__init__(self, root, bg=self.config["bg"], height=self.config["height"], width=self.config["width"])
        self.grid_propagate(False)
        self.rowconfigure(40, weight=1)
        self.grid(row=0, column=0)

        self.initUI()

    def load_icons(self):
        self.icons["house"] = ImageTk.PhotoImage(Image.open("./assets/house-white.png"))
        self.icons["list"] = ImageTk.PhotoImage(Image.open("./assets/list-white.png"))

    def initUI(self):
        self.logo("Memory Mender").grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.separator().grid(row=1, column=0)

        self.menu(
            icon=self.icons["house"],
            text="Home",
            command=lambda: self.switch_section_callback("Processing")
        ).grid(row=2, column=0)

        self.menu(
            icon=self.icons["list"],
            text="History",
            command=lambda: self.switch_section_callback("History")
        ).grid(row=3, column=0)

        self.separator().grid(row=41, column=0)
        self.footer("© 2024 Memory Mender").grid(row=42, column=0, padx=20, pady=20, sticky="w")

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
            height=self.config["separator_height"]
        )
    def menu(self, icon, text, command):
        menu_frame = tk.Frame(
            self,
            bg=self.config["bg"],
            height=self.config["menu_height"],
            width=self.config["width"]
        )
        menu_frame.grid_propagate(False)
        menu_frame.grid_rowconfigure(0, weight=1)

        icon_label = tk.Label(menu_frame, image=icon, bg=self.config["bg"])
        icon_label.grid(row=0, column=0, padx=20, sticky="w")

        text_label = tk.Label(menu_frame, text=text,fg=self.config["text_color"],bg=self.config["bg"],font=("Helvetica, 16"))
        text_label.grid(row=0, column=1, sticky="w")

        self.bind_menu_event(menu_frame, icon_label, text_label, command)

        return menu_frame
    def footer(self, text):
        return tk.Label(
            self,
            text=text,
            fg=self.config["text_color"],
            bg=self.config["bg"],
            font=("Helvetica, 10")
        )

    def bind_menu_event(self, menu_frame, icon_label, text_label, command):
        menu_frame.bind(
            "<Enter>",
            lambda e: (
                menu_frame.config(bg=self.config["menu_hover_bg"]),
                icon_label.config(bg=self.config["menu_hover_bg"]),
                text_label.config(bg=self.config["menu_hover_bg"])
            )
        )
        menu_frame.bind(
            "<Leave>",
            lambda e: (
                menu_frame.config(bg=self.config["bg"]),
                icon_label.config(bg=self.config["bg"]),
                text_label.config(bg=self.config["bg"])
            )
        )

        for widget in [menu_frame, icon_label, text_label]:
            widget.bind("<Button-1>", lambda e: command())