import tkinter as tk
from tkinter import messagebox
import math


def calcular_logaritmo_neperiano(valor):
    try:
        if not isinstance(valor, (int, float)):
            raise TypeError

        if valor < 0:
            raise ArithmeticError

        return math.log(valor)

    except ArithmeticError:
        messagebox.showerror(
            "Error",
            "El valor debe ser un número positivo para calcular el logaritmo"
        )

    except TypeError:
        messagebox.showerror(
            "Error",
            "El valor debe ser numérico para calcular el logaritmo"
        )

    return None


def calcular_raiz_cuadrada(valor):
    try:
        if not isinstance(valor, (int, float)):
            raise TypeError

        if valor < 0:
            raise ArithmeticError

        return math.sqrt(valor)

    except ArithmeticError:
        messagebox.showerror(
            "Error",
            "El valor debe ser un número positivo para calcular la raíz cuadrada"
        )

    except TypeError:
        messagebox.showerror(
            "Error",
            "El valor debe ser numérico para calcular la raíz cuadrada"
        )

    return None


def calcular():
    try:
        valor = float(txt_valor.get())

        logaritmo = calcular_logaritmo_neperiano(valor)
        raiz = calcular_raiz_cuadrada(valor)

        if logaritmo is not None:
            lbl_logaritmo.config(
                text=f"Logaritmo neperiano: {logaritmo:.4f}"
            )

        if raiz is not None:
            lbl_raiz.config(
                text=f"Raíz cuadrada: {raiz:.4f}"
            )

    except ValueError:
        messagebox.showerror(
            "Error",
            "El valor debe ser numérico"
        )


def limpiar():
    txt_valor.delete(0, tk.END)

    lbl_logaritmo.config(
        text="Logaritmo neperiano:"
    )

    lbl_raiz.config(
        text="Raíz cuadrada:"
    )

    txt_valor.focus()


# Ventana principal
ventana = tk.Tk()
ventana.title("Logaritmo y Raíz Cuadrada")
ventana.geometry("400x250")
ventana.resizable(False, False)

# Entrada
tk.Label(
    ventana,
    text="Valor numérico:"
).pack(pady=10)

txt_valor = tk.Entry(
    ventana,
    width=25
)
txt_valor.pack()

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=15)

btn_calcular = tk.Button(
    frame_botones,
    text="Calcular",
    width=12,
    command=calcular
)
btn_calcular.grid(row=0, column=0, padx=5)

btn_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    width=12,
    command=limpiar
)
btn_limpiar.grid(row=0, column=1, padx=5)

# Resultados
lbl_logaritmo = tk.Label(
    ventana,
    text="Logaritmo neperiano:"
)
lbl_logaritmo.pack(pady=5)

lbl_raiz = tk.Label(
    ventana,
    text="Raíz cuadrada:"
)
lbl_raiz.pack(pady=5)

ventana.mainloop()
