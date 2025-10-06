import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera app")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack()

ventana.mainloop()

def saludar():
    print("Hola")

boton = tk.Button(ventana,text="saludar", command=saludar)
boton.pack()

label = tk.label(root, text = "Hola", font = ("Arial", 14))
label.pack()

entrada = tk.Entry(root)
entrada.pack()

texto = entrada.get()