from core.config import selec_category
from outputs.bienvenida import saludo
from core.juego import assign_hide_word, revelar_palabra, create_word_space, indices_letra
from utils.utils import ascii_loader, limpiar_consola


#necesitamos palabras para adivinar
#necesitamos un grafico del muneco  ###
#mensaje de bienvenida ###
#espacio de la palabra 
#el usuario debe poder escribir una letra
#se valida la letra si pertenece a la palabra
#si la letra es correcta se anade al espacio de la palabra y sino el muneco se va armando
#el usuario tiene 6 vidas
#si se terminan las vidas y no se adivino la palabra este pierde
#si tiene vidas, mientras que adivino la palabra este gana

#Declarar diccionario de config del juego
configs = {
    "idioma": "no-value",
    "categoria": "no-value",
    "dificultad": "no-value"
}

#Declarar diccionario para las variables del juego(vida, espacio_palabra, letra, palabra, letras_jugadas, puntaje)
variables = {
    "vida": 6,
    "espacio_palabra": [],
    "letra": "no-value",
    "palabra": "no-value",
    "letras_jugadas": [],
    "puntaje": 0
}

#El usuario selecciona la categoria
print("Seleccione la categoria para inciar con el juego")
selec_category(configs)

#Seleccionar palabras escondida de ESA categoria
assign_hide_word(configs["categoria"], variables)

#1) Generar el espacio de la palabra selecionada, debe ser una lista. ejem: ["_", "_", "_"]
create_word_space(variables)

#Test juego
print("Si ya no desea jugar escriba (salir)")

letra = ""
while letra != "salir" and variables["vida"] != 0 and "_" in variables["espacio_palabra"] : 
  letra = input("Ingrese una letra: ")
  limpiar_consola()
  
  variables["espacio_palabra"] = revelar_palabra(variables["espacio_palabra"], variables["palabra"], letra)
  print(" ".join(variables["espacio_palabra"]))
  if len(indices_letra(variables["palabra"], letra)) == 0: # si el usuario se equivoca
    variables["vida"] -= 1

  print(f"\n \n Vidas restantes: {variables["vida"]}")
  ascii_loader(variables["vida"])






#Subir cambios
# git add .
# git commit -m "agregue que vida = 0"
# git push origin dev/Ana

#Bajar cambios
#git add .
#git pull origin main





