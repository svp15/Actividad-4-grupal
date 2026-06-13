import tkinter as tk
from tkinter import messagebox


class Vendedor:
    """
    Esta clase modela un vendedor con nombre, apellidos y edad.
    """

    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def verificar_edad(self, edad):
        if edad < 18:
            raise ValueError(
                "El vendedor debe ser mayor de 18 años."
            )

        if 0 <= edad < 120:
            self.edad = edad
        else:
            raise ValueError(
                "La edad no puede ser negativa ni mayor a 120."
            )


def calcular():
    try:
        nombre = txt_nombre.get()
        apellidos = txt_apellidos.get()
        edad = int(txt_edad.get())

        vendedor = Vendedor(nombre, apellidos)

        try:
            vendedor.verificar_edad(edad)

            messagebox.showinfo(
                "Edad",
                f"Edad registrada con éxito: {edad}"
            )

        except ValueError as e:
            messagebox.showerror(
                "Error",
                str(e)
            )

        # Mostrar siempre los datos
        messagebox.showinfo(
            "Nombre",
            f"Nombre del vendedor = {nombre}"
        )

        messagebox.showinfo(
            "Apellidos",
            f"Apellidos del vendedor = {apellidos}"
        )

        messagebox.showinfo(
            "Edad",
            f"Edad del vendedor = {edad}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingrese una edad válida."
        )


def limpiar():
    txt_nombre.delete(0, tk.END)
    txt_apellidos.delete(0, tk.END)
    txt_edad.delete(0, tk.END)
    txt_nombre.focus()


# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Vendedor")
ventana.geometry("350x250")
ventana.resizable(False, False)

# Nombre
tk.Label(
    ventana,
    text="Nombre del vendedor:"
).pack(pady=5)

txt_nombre = tk.Entry(ventana, width=30)
txt_nombre.pack()

# Apellidos
tk.Label(
    ventana,
    text="Apellidos del vendedor:"
).pack(pady=5)

txt_apellidos = tk.Entry(ventana, width=30)
txt_apellidos.pack()

# Edad
tk.Label(
    ventana,
    text="Edad del vendedor:"
).pack(pady=5)

txt_edad = tk.Entry(ventana, width=30)
txt_edad.pack()

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

ventana.mainloop()
