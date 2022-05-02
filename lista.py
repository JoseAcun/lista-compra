
lista = []
desision = 0
while True:
    desision = input("¿Que va a hacer?\n"
                                    "[1]. Agregar una nota\n"
                                    "[2]. Quitar una tarea\n"
                                   "[3]. Ver la lista\n"
                                   "[Q]. salir\n")

    if desision == "1":
    
        lista.append(input("Escriba su nueva tarea: \n"
                                    "\n"
                                    "\n"))
        print(lista)

        
    elif desision == "2":
        decide = int(input("Cual tarea quieres borrar iniciando desde el 0?\n"))
        lista.pop(decide)
        print(lista)
    elif desision == "3":
        i = 0

        while i < len(lista):
            print("* ""[{}]" .format(i+1),lista[i], " *")
            i = i + 1
            if i == len(lista):
                print("--------------")
    else:
        break




input("preciona enter para finalizar")


