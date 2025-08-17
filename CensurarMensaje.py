# Para esta demostración, sólo se usarán 3 palabras, pero una versión completa debería tener más.
palabras_prohibidas = {"estúpido":"*******", "pendejo":"*******", "idiota":"******"}


def censurar_mensaje(mensaje, prohibicion):
    for palabra, censura in prohibicion.items():
        mensaje = mensaje.replace(palabra.lower(), censura)
    return mensaje

testing = input("Escribe un mensaje: ")
result = censurar_mensaje(testing, palabras_prohibidas)
print(result)

