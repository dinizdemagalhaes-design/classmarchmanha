import tkinter as tk

janela = tk.Tk()
janela.title("Estrutura base")
janela.geometry("600x400")

# Configuração da grade da janela
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)

# Frame esquerdo (W)
frame_esquerdo = tk.Frame(janela, bg="lightblue")
frame_esquerdo.grid(row=0, column=0, rowspan=2, sticky="nsew")

label_esq = tk.Label(frame_esquerdo, text="Frame Esquerdo", bg="lightblue")
label_esq.pack(expand=True)

# Frame Direitp
frame_centro = tk.Frame(janela, bg="lightgreen")
frame_centro.grid(row=0, column=1, sticky="nsew")

label_centro = tk.Label(frame_centro, text="Frame Direito", bg="light green")
label_centro.pack(expand=True)

# Frame inferior Direito
frame_inferior = tk.Frame(janela, bg="yellow")
frame_inferior.grid(row=1, column=1, sticky="nsew")

label_inf = tk.Label(frame_inferior, text="Frame Inferior Direito", bg="yellow" )
label_inf.pack(expand=True)

janela.mainloop()
