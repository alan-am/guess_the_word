#funciones para manejar ajustes del juego
from pathlib import Path
from utils import utils

def selec_category(dic_configs):
    ''' Muestra lista de opciones de categorias al usuario para que seleccione una 
    y actualiza el diccionarios de configuraciones'''
    rute = Path("./banco_palabras") #representacion carpeta
    files = []

    selection = None
    i = 0 
    for file in rute.iterdir():
        if file.is_file():
            files.append(file.name)
            print(f'{i+1}. {file.stem}')
            i+=1

    selection = utils.validator_of_selection(1, len(files))

    dic_configs['categoria'] = files[selection - 1]

def seleccionar_categoria(configs):
    seleccion = None
    opciones = ["Animales", "Frutas"]
    print("> Selecciona la categoria de la palabra: ")
    for i in range(0, len(opciones)):
        print(f'{i+1}. {opciones[i]}')

    seleccion = int(input("> ")) - 1
    configs["categoria"] = opciones[seleccion]
    return configs
