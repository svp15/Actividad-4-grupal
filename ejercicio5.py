import tkinter as tk
from tkinter import messagebox

def leer_archivo():
    try:
        with open("prueba.txt", "rb") as archivo:
            contenido = archivo.read()

        texto = contenido.decode("utf-8")

        area_texto.delete("1.0", tk.END)
        area_texto.insert(tk.END, texto)

    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo prueba.txt")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Leer Archivo")

btn_leer = tk.Button(ventana, text="Leer Archivo", command=leer_archivo)
btn_leer.pack(pady=10)

area_texto = tk.Text(ventana, width=60, height=15)
area_texto.pack(padx=10, pady=10)

ventana.mainloop()
