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

#Saludo
def saludo():
    print("¡Bienvenido a uno de los mejores juegos en solitario!")
    print("Desestrésate o estrésate adivinando la palabra por tu cuenta y sin ayuda de nadie.")
    print("Sin más preámbulos… ¡COMENCEMOS CON EL JUEGO!")

saludo()

#banco de palabras
adivinar_palabra = ["Acuario","peces","tiburon","sirenas","orcas"]

#definicion de las vidas del usuario
vidas = 6

#Seleccion de la palabra escondida
palabra = adivinar_palabra[4]
#print(palabra)

#cuenta las letras
cantidad_letras = len(palabra)

#imprime el espacio de la palabra
print("_"*cantidad_letras)


#crear una funcion que una vez que el usuario haya adivinado todas las letras haga terminar el bucle

#verifica que la condicion de vidas este en el rango de 0-6
while(vidas <= 6 and vidas > 0):
    #Usuario coloca una letra y se imprime
    letra = input("Ingrese una letra: ")

    #validacion si la letra pertenece a la palabra, se le quite -1 o quede igual
    if letra in palabra:
        print("la letra es correcta")
    else:
        print("la letra es incorrecta")
        vidas = vidas-1


#Subir cambios
# git add .
# git commit -m "agregue que vida = 0"
# git push origin dev/Ana

#Bajar cambios
#git pull origin mai





