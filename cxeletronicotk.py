import tkinter as tk

def sacar():
    try:
        valor = int(entry_valor.get())
        total = valor
        ced = 50
        totalced = 0
        resultado = ""

        while True:
            if total >= ced:
                total -= ced
                totalced += 1
            else:
                if totalced > 0:
                    resultado += f"{totalced} cédula(s) de R${ced}\n"

                if ced == 50:
                    ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 1

                totalced = 0

                if total == 0:
                    break

        label_resultado.config(text=resultado)

    except ValueError:
        label_resultado.config(text="Digite um número válido!")

# Janela principal
root = tk.Tk()
root.title("Caixa Eletrônico 💸")
root.geometry("300x300")

# Título
label_titulo = tk.Label(root, text="Caixa Eletrônico", font=("Arial", 16))
label_titulo.pack(pady=10)

# Entrada
entry_valor = tk.Entry(root)
entry_valor.pack(pady=10)

# Botão
botao = tk.Button(root, text="Sacar", command=sacar)
botao.pack(pady=10)

# Resultado
label_resultado = tk.Label(root, text="", justify="left")
label_resultado.pack(pady=10)

# Rodar sistema
root.mainloop()
