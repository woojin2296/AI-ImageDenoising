import tkinter as tk
from components import Navbar, ProcessingSection, HistorySection

class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Memory Mender")
        self.geometry("1080x606-1920-900")

        # 현재 표시 중인 섹션 저장
        self.current_section = None

        # Navbar 추가
        self.addNavbar()

        # 섹션 컨테이너 추가
        self.section_container = tk.Frame(self, height=606, width=830)
        self.section_container.grid(row=0, column=1, sticky="nsew")

        # 섹션 추가
        self.processing_section = ProcessingSection(self.section_container)
        self.history_section = HistorySection(self.section_container)

        # 초기 섹션 설정
        self.show_section("Processing")

    def addNavbar(self):
        navbar = Navbar(self, switch_section_callback=self.show_section)
        navbar.grid(row=0, column=0)

    def addProcessingSection(self):
        processingSection = ProcessingSection(self)
        processingSection.grid(row=0, column=1)

    def addHistorySection(self):
        historySection = HistorySection(self)
        historySection.grid(row=0, column=1)

    def show_section(self, section_name):
        if self.current_section:
            self.current_section.grid_forget()

        # 새 섹션 표시
        if section_name == "Processing":
            self.current_section = self.processing_section
        elif section_name == "History":
            self.current_section = self.history_section

        self.current_section.grid(row=0, column=0, sticky="nsew")

