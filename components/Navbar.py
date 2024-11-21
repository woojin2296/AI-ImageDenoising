import tkinter as tk

class Navbar(tk.Frame):
    def __init__(self, root, switch_section_callback):
        self.height = 606
        self.width = 250
        self.bg = "#26282A"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        # 섹션 전환 콜백 함수 저장
        self.switch_section_callback = switch_section_callback

        # Navbar 내부 레이아웃 설정
        self.rowconfigure(40, weight=1)  # Footer를 맨 아래로 밀어내기 위해 마지막 행에 weight 설정
        self.columnconfigure(0, weight=1)  # Footer를 수평 중앙에 위치하도록 설정

        self.initUI()

    def initUI(self):
        self.setLogo(5, 0)

        self.setSeparator(9, 0, 250, 1)

        # Home 버튼: ProcessingSection으로 전환
        self.setMenu(15, 0, None, "Home", lambda: self.switch_section_callback("Processing"))

        self.setSeparator(19, 0, 250, 1)

        # History 버튼: HistorySection으로 전환
        self.setMenu(25, 0, None, "History", lambda: self.switch_section_callback("History"))

        self.setSeparator(29, 0, 250, 1)

        self.setSeparator(41, 0, 250, 1)
        self.setFooter(45, 0)

    def setLogo(self, row, column):
        self.logo = tk.Label(self, text="Memory Mender", fg="white", bg=self.bg, font=("Helvetica, 20"))
        self.logo.grid(row=row, column=column, sticky="w", padx=20, pady=20)

    def setSeparator(self, row, column, width, height):
        self.separator = tk.Frame(self, bg="#ffffff", width=width, height=height)
        self.separator.grid(row=row, column=column)

    def setMenu(self, row, column, icon, text, command):
        self.menuSection = tk.Button(self, bg=self.bg, fg="white", text=text, font=("Helvetica, 12"), command=command)
        self.menuSection.grid_propagate(False)
        self.menuSection.grid(row=row, column=column, sticky="w", padx=20, pady=20)

    def setFooter(self, row, column):
        self.footer = tk.Label(self, text="© 2021 Memory Mender", fg="white", bg=self.bg, font=("Helvetica, 10"))
        self.footer.grid(row=row, column=column, sticky="s", padx=20, pady=20)