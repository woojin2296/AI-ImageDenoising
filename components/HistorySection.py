import tkinter as tk

class HistorySection(tk.Frame):
    def __init__(self, root):
        self.height = 606
        self.width = 250
        self.bg = "#26282A"

        tk.Frame.__init__(self, root, bg=self.bg, height=self.height, width=self.width)
        self.grid_propagate(False)
        self.grid(row=0, column=0)

        # Navbar 내부 레이아웃 설정
        self.rowconfigure(40, weight=1)  # Footer를 맨 아래로 밀어내기 위해 마지막 행에 weight 설정
        self.columnconfigure(0, weight=1)  # Footer를 수평 중앙에 위치하도록 설정

        self.initUI()

    def initUI(self):
        self.setLogo(5, 0)

        self.setSeparator(9, 0, 250, 1)


        self.setMenu(15, 0, None, "Home", None)


        self.setSeparator(19, 0, 250, 1)

        self.setMenu(25, 0, None, "History", None)

        self.setSeparator(29, 0, 250, 1)

        self.setSeparator(41, 0, 250, 1)
        self.setFooter(45, 0)  # Footer를 마지막 행(40번)에 배치

    def setLogo(self, row, column):
        self.logo = tk.Label(self, text="Memory Mender", fg="white", bg=self.bg, font=("Helvetica, 20"))
        self.logo.grid(row=row, column=column, sticky="w", padx=20, pady=20)

    def setSeparator(self, row, column, width, height):
        self.separator = tk.Frame(self, bg="#ffffff", width=width, height=height)
        self.separator.grid(row=row, column=column)

    def setMargin(self, row, column, height):
        self.margin = tk.Frame(self, bg=self.bg, height=height)
        self.margin.grid(row=row, column=column)

    def setMenu(self, row, column, icon, text, command):
        self.menuSection = tk.Button(self, bg=self.bg, fg="white", text=text, font=("Helvetica, 12"), command=command)
        self.menuSection.grid_propagate(False)
        self.menuSection.grid(row=row, column=column, sticky="w", padx=20, pady=20)

    def setFooter(self, row, column):
        self.footer = tk.Label(self, text="© 2021 Memory Mender", fg="white", bg=self.bg, font=("Helvetica, 10"))
        self.footer.grid(row=row, column=column, sticky="s", padx=20, pady=20)

# 테스트 실행
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("850x650")
    Navbar(root)
    root.mainloop()