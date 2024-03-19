#Primeiro instale usando pip install deep_translator no Prompt
import customtkinter as ctk
from deep_translator import GoogleTranslator #importa a ferramenta de tradução

#funções -----------------

def traduzir(): 
    texto_para_traduzir = user_text.get()
    linguagem = lang_to_var.get()
    saida = GoogleTranslator(source='auto', target=linguagem).translate(texto_para_traduzir)
    translated_text.delete(0, 'end')
    translated_text.insert(0, saida)
    
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

janela = ctk.CTk()
janela.title('Tradutor Universal V1.0') 
janela.minsize(600,400)


ctk.CTkLabel(janela, text='Tradutor Universal V1.0', font=('Arial', 25, 'bold'), text_color='green').pack(pady=5)

ctk.CTkLabel(janela, text='Texto para traduzir', font=('Arial', 18, 'bold'), text_color='white').pack(pady=10)

user_text = ctk.CTkEntry(janela, height=50, width=400)
user_text.pack(pady=0)

ctk.CTkLabel(janela, text="Escolha a linguagem para traduzir", font=('Arial', 15, 'bold'), text_color="white").pack(pady=3)

lang_to_var=ctk.StringVar(value='english')
lang_list = GoogleTranslator().get_supported_languages()
lang_to = ctk.CTkOptionMenu(janela, values=lang_list, variable=lang_to_var)
lang_to.set('english')
lang_to.pack(pady=5)



ctk.CTkLabel(janela, text="Texto Traduzido", font=('Arial', 18, 'bold'), text_color="white").pack(pady=10)

translated_text = ctk.CTkEntry(janela, height=100, placeholder_text='O texto traduzido será mostrado aqui.')
translated_text.pack(pady=5)

translated_btn = ctk.CTkButton(janela, text="Traduzir", font=('Arial', 18, 'bold' ),command=traduzir)
translated_btn.pack(pady=10)

janela.mainloop()