#funciones para manejar ajustes del juego

def seleccionar_categoria(configs):
    seleccion = None
    opciones = ["Animales", "Frutas"]
    print("> Selecciona la categoria de la palabra: ")
    for i in range(0, len(opciones)):
        print(f'{i+1}. {opciones[i]}')

    seleccion = int(input("> ")) - 1
    configs["categoria"] = opciones[seleccion]
    return configs
