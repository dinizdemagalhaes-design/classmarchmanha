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


# janela principal
root = tk.Tk()
root.title("Caixa Eletrônico")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# título
label_titulo = tk.Label(root,text="Caixa Eletrônico",font=("Arial", 16, "bold"),bg="#f0f0f0")
label_titulo.place(relx=0.5, rely=0.1, anchor="center")

# texto do valor
label_valor = tk.Label(root,text="Digite o valor do saque:",font=("Arial", 11),bg="#f0f0f0")
label_valor.place(relx=0.5, rely=0.25, anchor="center")

# entrada
entry_valor = tk.Entry(root, font=("Arial", 12), justify="center")
entry_valor.place(relx=0.5, rely=0.35, anchor="center", relwidth=0.4)

# botão
botao_sacar = tk.Button(root,text="Sacar",font=("Arial", 11, "bold"),command=sacar)
botao_sacar.place(relx=0.5, rely=0.48, anchor="center", relwidth=0.25)

# resultado
label_resultado = tk.Label(root,text="",font=("Arial", 11),bg="#f0f0f0",justify="left")
label_resultado.place(relx=0.5, rely=0.75, anchor="center")

root.mainloop()
label_resultado.pack(pady=10)

# Rodar sistema
root.mainloop()
