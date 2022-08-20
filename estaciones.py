mesa=input('Digite el  mes del año')
mes=mesa.lower()

if mes=='enero' or mes == 'febrero' or mes== 'marzo':
    print(f' para el mes {mes} la estacion es invierno')
elif mes=='abril' or mes == 'mayo' or mes== 'junio':
    print(f' para el mes {mes} la estacion es primavera')
elif mes=='julio' or mes =='agosto' or mes=='septiembre':
    print(f'para el mes{mes} la estacion es verano')
elif mes =='octubre' or mes == 'noviembre' or mes== 'diciembre':
    print(f'para el mes {mes} la estacion es otoño ')
else:
    print(f'el mes {mes} es invalido ')