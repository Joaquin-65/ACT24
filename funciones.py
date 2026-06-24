
#Colección para almacenar temporalmente los personajes
personajes = []

def buscar(nombre):
    for i in range(len(personajes)):
        if personajes[i]["nombre"]==nombre:
            return i #retornamos la posición donde está
    return -1 #Si el personaje no se encuentra retorna -1

def agregar(nombre,clase,nivel):
    #Validar los datos
    if len(nombre.strip())==0 or len(nombre.strip())>20:
        print("Nombre no váldio")
        return
    elif buscar(nombre)>=0:
        print("Nombre ya existe")
        return
    elif clase not in ("Guerrero", "Mago", "Pícaro"):
        print("Clase no válida, debe ser Guerrero, Mago o Pícaro")
        return
    elif nivel<=0 or nivel>50:
        print("El nivel debe estar entre 1 y 50")
        return
    #Registrar personaje en la lista
    rango = "Recluta"
    if nivel>=30: rango = "Élite"
    pj = {"nombre":nombre,"clase":clase,"nivel":nivel,"rango":rango}
    personajes.append(pj)
    print("Personaje registrado")