import tkinter as tk
from tkinter import messagebox

class BMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Hesaplayıcı")

        self.label = tk.Label(self.root, text="BMI Hesaplayıcı")
        self.label.pack()

        # Yaş, boy ve kilo için etiketler ve giriş alanları oluşturma
        self.label_age = tk.Label(self.root, text="Yaş:")
        self.label_age.pack()
        self.entry_age = tk.Entry(self.root)
        self.entry_age.pack()

        self.label_height = tk.Label(self.root, text="Yükseklik (cm):")
        self.label_height.pack()
        self.entry_height = tk.Entry(self.root)
        self.entry_height.pack()

        self.label_weight = tk.Label(self.root, text="Ağırlık (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.pack()

        self.button = tk.Button(self.root, text="Hesapla", command=self.calculate_bmi)
        self.button.pack()

    def calculate_bmi(self):
        try:
            age = int(self.entry_age.get())
            height = int(self.entry_height.get())
            weight = int(self.entry_weight.get())
        except ValueError:
            messagebox.showerror("Hata", "Lütfen doğru bir sayısal değer girin.")
            return


        # BMI Hesapla
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)

        # BMI kategorisini göster
        if bmi <= 16:
            messagebox.showinfo("BMI Kategorisi", "Ciddi Zayıflık")
        elif 16 < bmi <= 17:
            messagebox.showinfo("BMI Kategorisi", "Hafif Zayıflık")
        elif 17 < bmi <= 18.5:
            messagebox.showinfo("BMI Kategorisi", "Orta Düzey Zayıflık")
        elif 18.5 < bmi <= 25:
            messagebox.showinfo("BMI Kategorisi", "Normal")
        elif 25 < bmi <= 30:
            messagebox.showinfo("BMI Kategorisi", "Fazla Kilolu")
        elif 30 <= bmi <= 35:
            messagebox.showinfo("BMI Kategorisi", "Obezite Sınıfı I")
        elif 35 <= bmi <= 40:
            messagebox.showinfo("BMI Kategorisi", "Obezite Sınıfı II")
        elif bmi > 40:
            messagebox.showinfo("BMI Kategorisi", "Obezite Sınıfı III")

    def run(self):
        self.root.mainloop()

# BMI sınıfını oluştur ve çalıştır
oyun = BMI()
oyun.run()