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

def saludo():
    print("¡Bienvenido a uno de los mejores juegos en solitario!")
    print("Desestrésate o estrésate adivinando la palabra por tu cuenta y sin ayuda de nadie.")
    print("Sin más preámbulos… ¡COMENCEMOS CON EL JUEGO!")

saludo()

adivinar_palabra = ["Acuario","peces","tiburon","sirenas","orcas"]
vidas = 6

palabra = adivinar_palabra[4]
#print(palabra)

cantidad_letras = len(palabra)

print("_"*cantidad_letras)

letra = input("Ingrese una letra: ")
print(letra)


#orcas -> palabra

#s -> letra

is_in_palabra = letra in palabra

if letra in palabra:
    print("la letra es correcta")
else:
    print("la letra es incorrecta")
    vidas = vidas-1




num = 6



vidas = vidas-1

vidas = 0 

#Subir cambios
# git add .
# git commit -m "agregue que vida = 0"
# git push origin dev/Ana

#Bajar cambios
#git pull origin main

peces = 4
