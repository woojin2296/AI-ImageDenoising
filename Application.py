import tkinter as tk
from components import Navbar, ProcessingSection, HistorySection

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Memory Mender")
        self.geometry("1080x606-1920-600")
        self.resizable(False, False)

        self.navbar = Navbar(self, switch_section_callback=self.show_section)
        self.navbar.grid(row=0, column=0)

        self.section_container = tk.Frame(self, height=606, width=830)
        self.section_container.grid(row=0, column=1)

        self.current_section = None
        self.show_section("Processing")

    def show_section(self, section_name):
        if self.current_section:
            self.current_section.grid_forget()

        if section_name == "Processing":
            self.current_section = ProcessingSection(self.section_container)
        elif section_name == "History":
            self.current_section = HistorySection(self.section_container)

        self.current_section.grid(row=0, column=0, sticky="nsew")

