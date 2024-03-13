import customtkinter as ct
import os

# FUNÇÕES
def desligar():
    try:
        os.system('shutdown /s /t 0')
    except Exception as e:
        print("Erro ao desligar:", e)

def reiniciar():
    try:
        os.system('shutdown /r /t 0')
    except Exception as e:
        print("Erro ao reiniciar:", e)

def bloquear():
    try:
        os.system('shutdown /l')
    except Exception as e:
        print("Erro ao bloquear:", e)

ct.set_appearance_mode('dark')

janela = ct.CTk("black")
janela.minsize(300,500)
janela.title("Bomba patch 💣💣💣")

titulo = ct.CTkLabel(janela, text="BOMBA PATCH V1.0", text_color="darkred")
titulo.pack()

btn1 = ct.CTkButton(janela, text="Desligar", fg_color="White", text_color="darkgray", width=200, height=200, command=desligar)
btn1.pack(pady=20)
btn2 = ct.CTkButton(janela, text="Reiniciar", fg_color="White", text_color="darkgray", width=200, height=200, command=reiniciar)
btn2.pack(pady=20)
btn3 = ct.CTkButton(janela, text="Bloquear", fg_color="White", text_color="darkgray", width=200, height=200, command=bloquear)
btn3.pack(pady=20)

janela.mainloop()
