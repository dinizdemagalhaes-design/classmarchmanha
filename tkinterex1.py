import tkinter as tk
'''criar janela'''
root = tk.Tk()
root.geometry("600x200")
root.title ("Ola Mundo")
'''cria frame'''
frame_principal = tk.Frame(root, height=200, width=600, bg="lightblue")
frame_principal.place(rely=0, relx=0)
'''cria texto'''
label_saudacao = tk.Label(frame_principal, text="Ola Mundo", bg="lightblue")
label_saudacao.place(rely=0, relx=0)
''''executa sistema'''
root.mainloop()
