# Desarrolla un programa en Python que permita gestionar una lista de tareas pendientes. 
# El programa debe cumplir con los siguientes requisitos:

# Debe permitir agregar nuevas tareas a la lista.
# Debe permitir marcar tareas como completadas, lo que las eliminará de la lista de tareas pendientes.
# Debe mostrar la lista actual de tareas pendientes.
# Debe proporcionar un menú interactivo que permita al usuario seleccionar entre las opciones anteriores y salir del programa.
# El menú debe presentar las siguientes opciones:

# Agregar tarea
# Marcar tarea como completada
# Mostrar tareas
# Salir

#tipos de datos abstractos o complejos:

tareas:list=[] #creando una lista vacia
menu=f"""
        ________MENU DE OPCIONES_________
        1.Agregar Tarea
        2.Marcar Tarea completa
        3.Mostrar Tarea
        4.Salir
        """
while True:
    print(menu)
    opcion=input("Ingresa la opcion que deseas realizar :")
    if opcion == "4":
        break
    elif opcion == "1":
        tarea=input("Ingrese una tarea: ")
        tareas.append(tarea)
        print(f"tarea {tarea} fue ingresada con exito!")
    elif opcion == "2":
        print(tareas)
        eliminar=input("escribe la tarea que deseas eliminar: ")
        el_eliminado=""
        for i,l in enumerate(tareas):
            if l == eliminar:
                el_eliminado=tareas.pop(i)
        print(f"la tarea {el_eliminado} fue eliminado de pendientes")
    elif opcion == "3":
        print(tareas)
        print(f"tines {len(tareas)} tareas pendientes")