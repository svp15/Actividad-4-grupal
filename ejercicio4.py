import tkinter as tk
from tkinter import messagebox


class EquipoLlenoException(Exception):
    pass


class DatoInvalidoException(Exception):
    pass


class Programador:

    def __init__(self, nombre, apellidos):
        self.validar_texto(nombre, "Nombre")
        self.validar_texto(apellidos, "Apellidos")

        self.nombre = nombre
        self.apellidos = apellidos

    @staticmethod
    def validar_texto(texto, campo):

        if len(texto) >= 20:
            raise DatoInvalidoException(
                f"{campo} no puede tener 20 o más caracteres."
            )

        if not texto.replace(" ", "").isalpha():
            raise DatoInvalidoException(
                f"{campo} debe contener solo letras."
            )


class EquipoMaratonProgramacion:

    MIN_PROGRAMADORES = 2
    MAX_PROGRAMADORES = 3

    def __init__(self, nombre_equipo,
                 universidad,
                 lenguaje,
                 tamano_equipo):

        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje = lenguaje
        self.tamano_equipo = tamano_equipo

        self.programadores = []

    def esta_completo(self):
        return len(self.programadores) == self.tamano_equipo

    def agregar_programador(self, programador):

        if len(self.programadores) >= self.tamano_equipo:
            raise EquipoLlenoException(
                "El equipo ya está completo."
            )

        self.programadores.append(programador)

    def __str__(self):
        texto = (
            f"Equipo: {self.nombre_equipo}\n"
            f"Universidad: {self.universidad}\n"
            f"Lenguaje: {self.lenguaje}\n"
            f"Tamaño: {self.tamano_equipo}\n\n"
            f"Programadores:\n"
        )

        for p in self.programadores:
            texto += f"- {p.nombre} {p.apellidos}\n"

        return texto


class Ventana:

    def __init__(self, root):

        self.root = root
        self.root.title("Maratón de Programación")

        self.equipo = None

        tk.Label(root, text="Nombre del equipo").grid(row=0, column=0)
        self.txt_equipo = tk.Entry(root)
        self.txt_equipo.grid(row=0, column=1)

        tk.Label(root, text="Universidad").grid(row=1, column=0)
        self.txt_universidad = tk.Entry(root)
        self.txt_universidad.grid(row=1, column=1)

        tk.Label(root, text="Lenguaje").grid(row=2, column=0)
        self.txt_lenguaje = tk.Entry(root)
        self.txt_lenguaje.grid(row=2, column=1)

        tk.Label(root, text="Tamaño (2 o 3)").grid(row=3, column=0)
        self.txt_tamano = tk.Entry(root)
        self.txt_tamano.grid(row=3, column=1)

        tk.Button(
            root,
            text="Crear Equipo",
            command=self.crear_equipo
        ).grid(row=4, column=0, columnspan=2, pady=5)

        tk.Label(root, text="Nombre").grid(row=5, column=0)
        self.txt_nombre = tk.Entry(root)
        self.txt_nombre.grid(row=5, column=1)

        tk.Label(root, text="Apellidos").grid(row=6, column=0)
        self.txt_apellidos = tk.Entry(root)
        self.txt_apellidos.grid(row=6, column=1)

        tk.Button(
            root,
            text="Agregar Programador",
            command=self.agregar_programador
        ).grid(row=7, column=0, columnspan=2, pady=5)

        tk.Button(
            root,
            text="Mostrar Equipo",
            command=self.mostrar_equipo
        ).grid(row=8, column=0, columnspan=2, pady=5)

    def crear_equipo(self):

        try:
            tamano = int(self.txt_tamano.get())

            if tamano < 2 or tamano > 3:
                raise ValueError

            self.equipo = EquipoMaratonProgramacion(
                self.txt_equipo.get(),
                self.txt_universidad.get(),
                self.txt_lenguaje.get(),
                tamano
            )

            messagebox.showinfo(
                "Éxito",
                "Equipo creado correctamente."
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "El tamaño del equipo debe ser 2 o 3."
            )

    def agregar_programador(self):

        if self.equipo is None:
            messagebox.showerror(
                "Error",
                "Primero debe crear el equipo."
            )
            return

        try:

            programador = Programador(
                self.txt_nombre.get(),
                self.txt_apellidos.get()
            )

            self.equipo.agregar_programador(programador)

            messagebox.showinfo(
                "Correcto",
                "Programador agregado."
            )

            self.txt_nombre.delete(0, tk.END)
            self.txt_apellidos.delete(0, tk.END)

            if self.equipo.esta_completo():
                messagebox.showinfo(
                    "Equipo Completo",
                    "El equipo ya está completo."
                )

        except (DatoInvalidoException,
                EquipoLlenoException) as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def mostrar_equipo(self):

        if self.equipo is None:
            messagebox.showwarning(
                "Aviso",
                "No existe un equipo creado."
            )
            return

        messagebox.showinfo(
            "Información del Equipo",
            str(self.equipo)
        )


if __name__ == "__main__":

    root = tk.Tk()
    app = Ventana(root)
    root.mainloop()
