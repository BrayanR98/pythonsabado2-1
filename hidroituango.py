# ENTRADA DEL PROBLEMA 

nivelAgua=int(input("Digita el nivel de agua de la presa: "))

#Proceso del problema 
if nivelAgua>=0 and nivelAgua<20 :
    print(f'el nivel de agua {nivelAgua} es muy bajo')
elif nivelAgua>=20 and nivelAgua<400:
    print(f'El nivel de agua {nivelAgua} es optimo')
elif nivelAgua>=400:
    print(f'el nivel de agua {nivelAgua} es peligroso')
else:
    print(f'el digito {nivelAgua} es invalido ')
