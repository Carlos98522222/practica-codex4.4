"""Prototipo mínimo: saludo personalizado para validar flujo CLI."""


def construir_mensaje(nombre: str) -> str:
    nombre_limpio = nombre.strip()
    if not nombre_limpio:
        return "Error: debes escribir un nombre válido."
    return f"Hola, {nombre_limpio}. Tu prototipo funciona correctamente."


if __name__ == "__main__":
    entrada = input("Escribe tu nombre: ")
    print(construir_mensaje(entrada))
