consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
        'Loja': {'consumos': (125, 65, 32, 130, 75, 62, 150, 55, 32, 120, 87, 42),'tarifa': 80},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Tena': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
informacion = {
    'costa': ('Guayaquil', 'Manta'),
    'sierra': ('Quito', 'Ambato', 'Loja'),
    'oriente': ('Tena', 'Nueva Loja')
}
def total_por_region(region):

    if region not in informacion.keys():
        return 'region no existe'

    ciudades_region = informacion[region]

    total_consumo = 0
    for ciudad_region in ciudades_region:
        for planta in consumo_energia.keys():
            for ciudad in consumo_energia[planta].keys():
                if ciudad_region ==  ciudad:
                    total_consumo += sum(consumo_energia[planta][ciudad]['consumos']) * consumo_energia[planta][ciudad]['tarifa']

    return total_consumo


def total_consumo_por_planta_ciudad(planta, ciudad):
    if planta not in consumo_energia.keys():
        return 'La planta ' + planta + ' no existe'

    if ciudad not in consumo_energia[planta].keys():
        return 'La planta ' + planta + ' no proveé energía a la ciudad de ' + ciudad

    total_consumo = sum(consumo_energia[planta][ciudad]['consumos'])
    return total_consumo

op = -1
def menu():
    print('<1>. Total de Energía Consumida por planta y Ciudad')
    print('<2>. Total de Energia por Ciudad ')
    print('<3>. Dinero Recaudado por Región ')
    print('<0>. Salir ')
while op != 0:
    menu()
    op = int(input('Ingrese una opción:'))

    if op == 1:
        planta = input('Ingrese el nombre de la planta (Coca Codo Sinclair, Sopladora):')
        ciudad = input(str('Ingrese nombre de la ciudad:'))

        total = total_consumo_por_planta_ciudad(planta, ciudad)
        
        if type(total) == int:
            print('El consumo de energía en la ciudad de {} fue de {} MWh en la planta {}'.format(ciudad, total, planta))
        else:
            print(total)

    elif op == 2:
        ciudad = input('Ingrese nombre de la ciudad:')
        if ciudad in consumo_energia['Sopladora'].keys(): 
            Sopla=sum(consumo_energia['Sopladora'][ciudad]['consumos'])
            print('La sopladora da:',Sopla,'mwb')

            if ciudad in consumo_energia['Coca Codo Sinclair'].keys():
                Cocacos=sum(consumo_energia['Coca Codo Sinclair'][ciudad]['consumos'])
                print('La Coca Codo da:',Cocacos,'mwb') 
            else:
                print('error')
            

    elif op == 3:
        region = input('Ingrese la región:')
        total = total_por_region(region)
        print(region, ':', total, '\n')