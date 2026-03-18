import tkinter as tk

# Criando a janela principal
janela = tk.Tk()
janela.title("Estrutura do Formulário")
janela.geometry("500x400")

# Frame superior (azul)
frame_topo = tk.Frame(janela, bg="lightblue")
frame_topo.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.2)

label_topo = tk.Label(frame_topo, text="Frame superior", bg="lightblue", font=("Arial Bold", 18))
label_topo.place(relx=0.5, rely=0.5, anchor="center")

# Frame do meio (verde)
frame_meio = tk.Frame(janela, bg="lightgreen")
frame_meio.place(relx=0.05, rely=0.30, relwidth=0.9, relheight=0.4)

label_meio = tk.Label(frame_meio, text="Frame do meio", bg="lightgreen", font=("Arial Bold", 18))
label_meio.place(relx=0.5, rely=0.5, anchor="center")

# Frame inferior (amarelo)
frame_baixo = tk.Frame(janela, bg="yellow")
frame_baixo.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.20)

label_baixo = tk.Label(frame_baixo, text="Frame inferior", bg="yellow", font=("Arial bond", 18))
label_baixo.place(relx=0.5, rely=0.5, anchor="center")

janela.mainloop()
