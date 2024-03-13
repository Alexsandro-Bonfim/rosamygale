import customtkinter as ct

# funções
def calcular_imc():
    Peso = int(peso.get())
    Altura = float(altura.get())
    Nome = nome.get()
    imc = Peso / (Altura * Altura)

    if imc < 18:
        resultado.configure(text=f'Senhor(a) {Nome}, seu imc está registrado em {imc:.2f}. Estás visivelmente abaixo do peso.')
    elif 18 <= imc < 25:
        resultado.configure(text=f'Senhor(a) {Nome}, seu imc está registrado em {imc:.2f}. Seu peso é ideal.')
    elif 25 <= imc < 30:
        resultado.configure(text=f'Senhor(a) {Nome}, seu imc está registrado em {imc:.2f}. Estás levemente acima do peso.')
    elif 30 <= imc < 35:
        resultado.configure(text=f'Senhor(a) {Nome}, seu imc está registrado em {imc:.2f}. Estás com obesidade grau I. Por favor, procure um médico.')
    elif 35 <= imc < 40:
        resultado.configure(text=f'Senhor(a) {Nome}, seu imc está registrado em {imc:.2f}. Estás com obesidade severa. É muito preocupante.')
    else:
        resultado.configure(text=f'Senhor(a) {Nome}, seu imc está registrado em {imc:.2f}. Obesidade mórbida.')

# fim das funções. Abaixo vem a janela.
ct.set_appearance_mode('dark')
janela = ct.CTk()
janela.minsize(450, 520)
janela.maxsize(980, 1260)
janela.title('aplicativo_saude')

# título
Título = ct.CTkLabel(janela, text='Calculadora de imc', font=('Arial', 25))
Título.pack(padx=10, pady=10)

# nome
nome = ct.CTkEntry(janela, placeholder_text="Digite o seu nome", width=400, height=25)
nome.pack(padx=10, pady=10)

# peso
peso = ct.CTkEntry(janela, placeholder_text="Digite o seu peso", width=400, height=25)
peso.pack(padx=10, pady=10)

# altura
altura = ct.CTkEntry(janela, placeholder_text="Digite a sua altura", width=400, height=25)
altura.pack(padx=10, pady=10)

# botão
button = ct.CTkButton(janela, text="Calcular", command=calcular_imc)
button.pack(padx=10, pady=10)

# resultado
resultado = ct.CTkLabel(janela, text='', text_color='white', font=('Arial', 20))
resultado.pack(pady=20)

# encerrando a janela
janela.mainloop()
