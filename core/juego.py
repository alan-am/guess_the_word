import random
# funciones de lógica del juego: progreso, errores, etc.

def indices_letra(word, letter):
    '''Recibe una letra, una palabra y 
    devuelve una lista de indices en donde se encuentra la letra(puede estar vacia)'''
    indices_encontrados = []
    letter_normalized = normalizar_letra(letter)
    if letter_normalized in word :
        for i in range(0, len(word)):
            word_letter = word[i]
            if word_letter == letter_normalized:
                indices_encontrados.append(i)

    return indices_encontrados


def normalizar_letra(letter):
    '''Recibe una letra, la convierte a minúscula, elimina tildes y espacios,
    ojo validar previamente con regex que sea letras del abecedario'''

    letter_normalized = letter.lower().strip()
    vocales_con_tildes = ["á", "é", "í", "ó", "ú"]
    if (letter_normalized in vocales_con_tildes):
        if letter_normalized == "á":
            letter_normalized = "a"

        elif letter_normalized == "é":
            letter_normalized = "e"

        elif letter_normalized == "í":
            letter_normalized = "i"

        elif letter_normalized == "ó":
            letter_normalized = "o"

        elif letter_normalized == "ú":
            letter_normalized = "u"
    print(letter_normalized)
    return letter_normalized


def revelar_palabra(word_space, word, letter):
    '''Actualiza el espacio de la palabra con las letras que se vayan adivinando'''
    indices = indices_letra(word, letter)
    for indice in indices:
        word_space[indice] = letter
    return word_space


def get_words_category(category):
    '''Lee el archivo de la categoria provista y retorna una lista de las palabras
    del archivo'''
    list = []
    with open("banco_palabras/"+category,"r") as file:
        for word in file:
            list.append(word.strip())
    
    return list


def assign_hide_word(category, dic_variables):
    words = get_words_category(category)
    '''Realiza un sorteo al azar , selecciona una palabra y la asigna al diccionario
    correspondiente'''
    random_num = random.randint(0, len(words) - 1)
    selected_word = words[random_num]
    dic_variables["palabra"] = selected_word

def create_word_space(variables):
    '''Cuenta las letras para generar el espacio de la palabra'''
    palabra = variables["palabra"]
    letras = len(palabra)
    variables["espacio_palabra"] = ["_"] * letras
    



# TESTS 

# indices_letra, normalizar_letra
# palabra= "perro"
# letra = None
# while letra != "salir":

#     letra = input("> Escriba una letra de la A-Z: ")
#     print(indices_letra(palabra, letra))


#revelar_palabra
# palabra = "perro"
# word_space = ["_", "_", "_", "_", "_"]

# while letra != "salir":

#     letra = input("> Escriba una letra de la A-Z: ")
#     word_space = revelar_palabra(word_space, palabra, letra)
#     print("".join(word_space))



#get_wprds_category
#print(get_words_category("banco_palabras/animales.txt"))
