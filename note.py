import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
import base64
from tkinter import  END


def encode(key,clear):
    enc = []
    for i in range(len(clear)):
        key_C = key[i % len(key)]
        enc_c = chr(ord(clear[i])+ord(key_C) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode(key,enc):
    dec = []
    enc = base64.urlsafe_b64encode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc [i])-ord(key_c) % 256))
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt_notes():
    title = title_entery.get()
    message = title_text.get("1.0",END)
    master_secret = title_entery3.get()

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
            messagebox.showinfo(title="Error!", message="Please enter all information.")
    else:
        message_encrypted = encode(master_secret, message)

        try:
            with open("mysecret.txt", "a") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        except FileNotFoundError:
            with open("mysecret.txt", "w") as data_file:
                data_file.write(f'\n{title}\n{message_encrypted}')
        finally:
            title_entery.delete(0, END)
            title_entery3.delete(0, END)
            title_text.delete("1.0",END)




def decrypt_notes():
    message_encrypted = title_text.get("1.0",)
    secret = title_entery3.get()

    if len(message_encrypted) == 0 or len(secret) == 0:
        messagebox.showinfo(title="Error!",message="please enter")
    else:
        try:
            decrypdt_message = decode(secret,message_encrypted)
            title_text.delete("1.0",END)
            title_text.insert("1.0",decrypdt_message)
        except:
            messagebox.showinfo(title="error!",message="Please make sure of encrypted info")



pencere = tk.Tk()
pencere.title("secret note")
pencere.geometry("400x700+100+50")
pencere.iconbitmap("project.ico")

resim = PhotoImage(file="project.png")
resim_kucuk = resim.subsample(10,10)
etiket1 = tk.Label(text="etiket",image=resim_kucuk)
etiket1.pack(pady=50)
etiket1.pack_configure(anchor=tk.N)

title_label = tk.Label(text="enter your title")
title_label.pack()
title_entery = tk.Entry(width=30)
title_entery.pack()

title_label2 = tk.Label(text="enter your secret",font=("arial",10,"normal"))
title_label2.pack()

title_text = tk.Text(width=37,height=17)
title_text.pack()

title_label3 = tk.Label(text="enter master key",font=("arial",10,"normal"))
title_label3.pack()
title_entery3 = tk.Entry(width=30)
title_entery3.pack()



title_save_encrypt = tk.Button(text="save & encrypt",width=20,command=save_and_encrypt_notes)
title_save_encrypt.pack(pady=20)

title_decrypt = tk.Button(text="decrypt",width=10,command=decrypt_notes)
title_decrypt.pack(pady=10)


pencere.mainloop()