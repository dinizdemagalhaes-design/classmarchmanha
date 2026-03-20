import tkinter  as tk


#Button
def button_clicked():
    print("Start")


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("600x400")





#Frame Superior
frame_topo =tk.Frame(root, bg="lightyellow")
frame_topo.place( relx=0.05, rely=0.05, relwidth=0.9, relheight=0.7)


#Frame Inferior
frame_inferior = tk.Frame(root, bg="lightyellow")
frame_inferior.place(anchor='center',relx=0.5, rely=0.85, relwidth=0.8, relheight=0.2)


#Criar botao Start
button = tk.Button(frame_inferior, text="Start", command=button_clicked, anchor= "center", bg="green", fg="white",height=2)
button.place(relx=0.5, rely=0.5, relwidth=0.3)

#Criar botao Reset
button = tk.Button(frame_inferior, text="Reset", command=button_clicked, anchor= "center", bg="red", fg="white",height=2)
button.place(relx=0.5, rely=0.05, relwidth=0.3)


root.mainloop()
