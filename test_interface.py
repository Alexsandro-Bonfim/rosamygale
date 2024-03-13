import customtkinter as ct

ct.set_appearance_mode('dark')

janela = ct.CTk('#1a6299')
janela.minsize(500, 500)
janela.maxsize(1000, 700)
janela.title('Tela de login')

titulo = ct.CTkLabel(janela, text="Tela de login", bg_color="white", text_color="#023b5e", font=('arial', 30, 'bold'))
titulo.pack(pady=20)

login = ct.CTkEntry(janela, placeholder_text="Digite seu login", width=350, height=50)
login.pack(pady=20)

senha = ct.CTkEntry(janela, placeholder_text="Digite sua senha", width=350, height=50, show='♠')
senha.pack(pady=20)

lembrar = ct.CTkCheckBox(janela, text="Lembrar Login", text_color='white')
lembrar.pack()

botao = ct.CTkButton(janela, text="Login", text_color="white")
botao.pack(pady=20)

janela.mainloop()
