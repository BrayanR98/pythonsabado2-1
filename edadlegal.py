edad = int(input('Digite su edad: '))

if edad>=0 and  edad<100:
    if edad==0 and edad<=14:
        print(f'para su edad {edad} en colombia es un niño')
    elif edad>=15 and edad<=28:
        print(f'para su edad {edad} en colombia es un joven')
    elif edad>=29 and edad<=60:
        print(f'para su edad {edad} en colombia es un adulto ')
    elif edad>60:
        print(f'para su edad {edad} en colombia es un adulto mayor')
else:
    print(f'{edad} dato invalido')