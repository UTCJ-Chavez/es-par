"""Módulo para determinar si un número entero es par."""


def es_par(numero):
    """Indica si un número entero es par.

    Args:
        numero (int): Número entero a evaluar.

    Returns:
        bool: True si el número es par, False si es impar.

    Raises:
        TypeError: Si ``numero`` no es un entero (se rechazan también
            los booleanos, los decimales y el texto).
    """
    if isinstance(numero, bool) or not isinstance(numero, int):
        raise TypeError("El número debe ser un entero.")
    return numero % 2 == 0


def main():
    """Pide un número por consola e indica si es par o impar."""
    texto = input("Introduce un número entero: ")
    try:
        numero = int(texto)
    except ValueError:
        print("Entrada inválida: debes escribir un número entero.")
        return
    if es_par(numero):
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")


if __name__ == "__main__":
    main()
