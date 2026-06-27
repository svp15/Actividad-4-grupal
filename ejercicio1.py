import tkinter as tk
from tkinter import messagebox


def calcular():
    try:
        messagebox.showinfo("Try 1", "Ingresando al primer try")

        numerador = float(txt_numerador.get())
        denominador = float(txt_denominador.get())

        cociente = numerador / denominador

        messagebox.showinfo(
            "Resultado",
            f"Después de la división\nCociente = {cociente}"
        )

        lbl_resultado.config(text=f"Cociente: {cociente}")

    except ZeroDivisionError:
        messagebox.showerror("Except 1", "División por cero")
        lbl_resultado.config(text="Cociente: Error")

    finally:
        messagebox.showinfo("Finally 1", "Ingresando al primer finally")

    try:
        messagebox.showinfo("Try 2", "Ingresando al segundo try")

        objeto = None

        objeto.toString()

        messagebox.showinfo("Mensaje", "Imprimiendo objeto")

    except ZeroDivisionError:
        messagebox.showerror("Except 2", "División por cero")

    except Exception:
        messagebox.showwarning("Except 2", "Ocurrió una excepción")

    finally:
        messagebox.showinfo("Finally 2", "Ingresando al segundo finally")


def limpiar():
    txt_numerador.delete(0, tk.END)
    txt_denominador.delete(0, tk.END)
    lbl_resultado.config(text="Cociente:")
    txt_numerador.focus()


ventana = tk.Tk()
ventana.title("Try - Except - Finally")
ventana.geometry("350x250")

tk.Label(ventana, text="Numerador").pack(pady=5)
txt_numerador = tk.Entry(ventana)
txt_numerador.pack()

tk.Label(ventana, text="Denominador").pack(pady=5)
txt_denominador = tk.Entry(ventana)
txt_denominador.pack()

frame = tk.Frame(ventana)
frame.pack(pady=15)

btn_calcular = tk.Button(frame, text="Calcular", command=calcular)
btn_calcular.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(frame, text="Limpiar", command=limpiar)
btn_limpiar.grid(row=0, column=1, padx=5)

lbl_resultado = tk.Label(
    ventana,
    text="Cociente:",
    font=("Arial", 12, "bold")
)
lbl_resultado.pack(pady=10)

ventana.mainloop()
