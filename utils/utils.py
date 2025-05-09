from pathlib import Path

def validator_of_selection(min, max):
    '''Valida la seleccion del usuario que este en el rango correcto'''
    selec = input('> ')
    while not selec.isdigit() or int(selec) < min or int(selec) > max:
        print(f'Invalid Selection, it has to be a number from {min} to {max}.')
        selec = input('> ')
        
    return int(selec) 

def ascii_loader(vidas):
    '''imprime un ascii del ahorcado , dependiendo de cuantas vidas tenga el usuario'''
    rute = Path("ascii")/f"{vidas}.txt"

    if  not rute.exists():
        print(f"Archivo: {rute} no encontrado.")
    else:
        with open(rute,"r") as file:  
             print(file.read())



#TESTS

#validator_of_selection
# print("Ingrese un numero del 1 al 6")
# validator_of_selection(1, 6)


#ascii_loader(7)

