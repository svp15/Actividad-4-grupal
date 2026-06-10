# codigo numero 1:

def main():
    # Primer bloque try
    try:
        print("Ingresando al primer try")
        cociente = 10000 / 0  # Se lanza una excepción
        print("Después de la división")  # Esta instrucción nunca será ejecutada
    except ZeroDivisionError:
        print("División por cero")  # Se imprime en pantalla este mensaje
    finally:
        # La sentencia finally siempre se ejecuta, ocurra o no una excepción
        print("Ingresando al primer finally")

    # Segundo bloque try
    try:
        print("Ingresando al segundo try")
        objeto = None
        objeto.toString()  # Se lanza una excepción
        # Esta instrucción nunca será ejecutada porque se lanzó una excepción
        print("Imprimiendo objeto")
    except ZeroDivisionError:
        # La excepción lanzada no es de este tipo
        print("División por cero")
    except Exception:
        # Se captura la excepción
        print("Ocurrió una excepción")  # Se imprime en pantalla este mensaje
    finally:
        # La sentencia finally siempre se ejecuta, ocurra o no una excepción
        print("Ingresando al segundo finally")


if __name__ == "__main__":
    main()

# codigo numero 2:

def main():
    try:
        texto = "Programación"

        caracter = texto[14]  # Índice fuera de rango

        print(caracter)

    except IndexError:
        print("Índice de string por fuera del límite")


if __name__ == "__main__":
    main()

# codigo numero 3:

def main():
    try:
        numero = int("Número")  # Conversión inválida

        print(numero)

    except ValueError:
        print("Excepción de formato de número")

    finally:
        print("Ingresando al finally")


if __name__ == "__main__":
    main()
