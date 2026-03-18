
import tkinter as tk

janela = tk.Tk()
janela.title("Estrutura VS Code")
janela.geometry("800x500")

# 🔵 Explorador (lado esquerdo)
explorador = tk.Frame(janela, bg="lightblue")
explorador.place(relx=0, rely=0, relwidth=0.2, relheight=1)

# 🟢 Área principal (direita)
# 🟢 Topo - páginas de código
topo = tk.Frame(janela, bg="green")
topo.place(relx=0.2, rely=0, relwidth=0.8, relheight=0.1)

# 🟩 Editor de código (meio)
editor = tk.Frame(janela, bg="lightgreen")
editor.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.7)

# 🟡 Terminal (baixo)
terminal = tk.Frame(janela, bg="yellow")
terminal.place(relx=0.2, rely=0.8, relwidth=0.8, relheight=0.2)

# Labels só pra identificar (opcional)
tk.Label(explorador, text="Explorador", bg="lightblue").pack()
tk.Label(topo, text="Páginas de Código", bg="green", fg="white").pack()
tk.Label(editor, text="Editor de Código", bg="lightgreen").pack()
tk.Label(terminal, text="Terminal", bg="yellow").pack()

janela.mainloop(
