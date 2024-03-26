#Alunos: Alexsandro Bonfim & Gabriel Marçal
import customtkinter as ctk

class Chaocipher:
    def __init__(self, key1, key2):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key1 = key1.upper()
        self.key2 = key2.upper()
        
    def encode(self, texto_a_codificar):
        text = texto_a_codificar.get()
        result = ''
        for char in text.upper():
            if char in self.alphabet:
                index = self.key1.find(char)
                result += self.key2[index]
            elif char == ' ':  # Verifica se é um espaço
                result += ' '   # Adiciona o espaço ao resultado sem alterá-lo
        texto_codificado.delete(0, 'end')
        texto_codificado.insert(0, result)

    def decode(self, text):
        result = ''
        for char in text.upper():
            if char in self.alphabet:
                index = self.key2.find(char)
                result += self.key1[index]
            elif char == ' ':  # Verifica se é um espaço
                result += ' '   # Adiciona o espaço ao resultado sem alterá-lo
        return result

def codificar():
    texto_codificado.delete(0, 'end')
    texto_codificado.insert(0, cipher.encode(texto_a_codificar))

def decodificar():
    texto_descodificado.delete(0, 'end')
    texto_descodificado.insert(0, cipher.decode(texto_a_descodificar.get()))

ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.geometry('700x550')

ctk.CTkLabel(janela, text="Digite o texto que deseja codificar").pack(pady=5)
texto_a_codificar = ctk.CTkEntry(janela, height=50, width=400, placeholder_text="Digite o texto aqui")
texto_a_codificar.pack(pady=20)

codi = ctk.CTkButton(janela, text="Codificar", command=codificar)
codi.pack(pady=10)

texto_codificado = ctk.CTkEntry(janela, height=50, width=400, placeholder_text="Texto codificado")
texto_codificado.pack(pady=20)

ctk.CTkLabel(janela, text="Digite o texto que deseja descodificar").pack(pady=5)

texto_a_descodificar = ctk.CTkEntry(janela, height=50, width=400, placeholder_text="Digite o texto aqui")
texto_a_descodificar.pack(pady=20)

descodi = ctk.CTkButton(janela, text="Descodificar", command=decodificar)
descodi.pack(pady=10)

texto_descodificado = ctk.CTkEntry(janela, height=50, width=400, placeholder_text="Texto descodificado")
texto_descodificado.pack(pady=20)

cipher = Chaocipher('HXUCZVAMDSLKPEFJRIGTWOBNYQ', 'PTLNBQDEOYSFAVZKGJRIHWXUMC')

janela.mainloop()
