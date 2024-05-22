# Tenemos la pantalla del móvil bloqueada. 
# Partiendo de un PIN_SECRETO, intentaremos desbloquear la pantalla. 
# Tenemos hasta 3 intentos. Simula el proceso con Python. En caso de acceder, 
# lanza al usuario login correcto. Sino, llamando ala policía.

pantalla_bloqueo=f"""
_______________________________
|                              |       
|                              |
|                              |
|                              |
|   'INGRESE SU PIN SECRETO'   |
|    _____________________     |
|    | * * * * *  * * *  |     |
|    _____________________     |
|                              |
|                              |
|                              |
|                              |
________________________________ 
"""
print(pantalla_bloqueo)
numero_intentos:int=1
pin_correcto=1234
while numero_intentos <=3:
    pin_secreto=int(input("INGRESE EL PIN SECRETO: "))
    if pin_secreto != pin_correcto:
        print(f"""
            numero de intento {numero_intentos} erroneo
            'LLAMANDO A LA POLICIA'
            """)
        numero_intentos+=1
        continue
    else:
        print("login correcto")
        break
    
