import tkinter as tk
from PIL import Image, ImageTk

class ProcessingSection(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root, bg="#000000", height=606, width=830)
        self.grid_propagate(False)
        self.grid(row=0, column=1)

        # 이미지 섹션 설정
        self.image_Section = tk.Frame(self, bg="#26282A", height=500, width=810)
        self.image_Section.grid_propagate(False)
        self.image_Section.grid(row=0, column=0, pady=10, padx=10)

        # 이미지 로드 및 크기 조정
        self.before_image = self.load_and_resize_image("image/img3.jpeg", 810, 500)
        self.after_image = self.load_and_resize_image("image/img2.jpg", 810, 500)

        # 이미지 레이블 생성
        self.image_label = tk.Label(self.image_Section, image=self.before_image, bg="#26282A", fg="#FFFFFF")
        self.image_label.grid(row=0, column=0, sticky="nsew")  # 중앙 정렬

        # 섹션 레이아웃 설정
        self.image_Section.grid_rowconfigure(0, weight=1)
        self.image_Section.grid_columnconfigure(0, weight=1)

        # 인터페이스 섹션
        self.interface_Section = tk.Frame(self, bg="#26282A", height=76, width=810)
        self.interface_Section.grid(row=1, column=0, padx=10)

    def load_and_resize_image(self, path, max_width, max_height):
        """이미지를 로드하고 섹션 크기에 맞게 비율을 유지하며 크기 조정"""
        img = Image.open(path)
        img.thumbnail((max_width, max_height), Image.ANTIALIAS)  # 섹션 크기에 맞게 조정
        return ImageTk.PhotoImage(img)

# 테스트 실행
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("850x650")
    ProcessingSection(root)
    root.mainloop()