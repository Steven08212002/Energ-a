consumo_energia = {
    'Coca Codo Sinclair':{
        'Quito': {'consumos': (400, 432, 400, 420, 432, 460, 432, 400, 432, 300, 213), 'tarifa': 65},
        'Guayaquil': {'consumos': (120, 55, 32, 120, 75, 32, 150, 55, 32, 120, 97, 32),'tarifa': 84},
    },
    'Sopladora': {
        'Guayaquil':{ 'consumos': (310, 220, 321, 310, 220, 321, 310, 220, 321, 310, 220, 321),'tarifa':55},
        'Quito': { 'consumos': (400, 432, 587, 400, 432, 587, 400, 432, 587, 400, 432, 587),'tarifa': 79},
        'Loja': { 'consumos': (50, 32, 32, 50, 32, 32, 50, 32, 32, 50, 32, 32),'tarifa': 32},
 },
}
tot_coca_codo_g = (120 + 55 + 32 + 120 + 75 + 32 + 150 + 55 + 32 + 120 + 97 + 32)
tot_coca_codo_q = (400 + 432 + 400 + 420 + 432 + 460 + 432 + 400 + 432 + 300 + 213)
tot_sopladora_g = (310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321 + 310 + 220 + 321)
tot_sopladora_q = (400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587 + 400 + 432 + 587)
tot_sopladora_l = (50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32 + 50 + 32 + 32)

informacion = {
 'Costa': ('Guayaquil', 'Manta'),
 'Sierra': ('Quito', 'Ambato', 'Loja'),
 'Oriente': ('Tena', 'Nueva Loja')
}

Costa = tot_coca_codo_g + tot_sopladora_g
Sierra = tot_sopladora_q + tot_coca_codo_q + tot_sopladora_l
Oriente = ('No hay planta en el Oriente')

print('''
    ===============================
          PLANTAS ENERGÉTICAS
    ===============================
    ''')
print('<1>. Total de MWh en Planta y ciudad')
print('<2>. Total de energía por ciudad')
print('<3>. Dinero recaudado por Región')
print('<4>. Escriba (salir) para salir')
opcion = input('Elija una opcion del 1 al 4: ')

if opcion == 'salir':
    exit

#1. Solicite al usuario el nombre de una planta y de una ciudad y presente el total de
#megavatios de consumos para dicha ciudad en dicha planta.
elif opcion == '1':
    
    print('''
    ===============================
         TOTAL DE MWh
               PLANTAS
    Coca Codo Sinclair, Sopladora
              CIUDADES
    Guayaquil, Quito, Loja
    ===============================
    ''')

    n_planta = input('Ingrese el nombre de la planta igual a la parte superior: ')

    if n_planta == 'Coca Codo Sinclair':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MWh de consumo en Coca Codo Sinclair, Quito: ', tot_coca_codo_q, 'MWh')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de MWh de consumo en Coca Codo Sinclair, Guayaquil: ', tot_coca_codo_g, 'MWh')
            print('Con tarifa de: ', consumo_energia['Coca Codo Sinclair']['Guayaquil']['tarifa'])
        elif n_ciudad =='Loja':
            print("No hay planta de Coca Codo Sinclair en Loja")
    print()

    if n_planta == 'Sopladora':
        n_ciudad = input('Ingrese el nombre de la ciudad: ')

        if n_ciudad == 'Quito':
            print('Total de MWh de consumo en Sopladora, Quito: ', tot_sopladora_q, 'MWh')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Quito']['tarifa'])
        elif n_ciudad == 'Guayaquil':
            print('Total de MWh de consumo en Sopladora, Guayaquil: ', tot_sopladora_g, 'MWh')
            print('Con tarifa de: ', consumo_energia['Sopladora']['Guayaquil']['tarifa'])
        elif n_ciudad == 'Loja':
            print('Total de MWh de consumo en Sopladora, Loja: ', tot_sopladora_l)
            print('Con tarifa de: ', consumo_energia['Sopladora']['Loja']['tarifa'])
        else:
            print("Digite correctamente la primera letra en mayúscula")

    exit
    

    

#2. Solicite al usuario el nombre de una ciudad y presente un nuevo diccionario cuyas claves
#son los nombres de las plantas generadoras y el valor es el total megavatios que cada
#planta le ha dado a ciudad. Si la planta no entrega energía a la ciudad entonces esa planta
#no debería aparecer en el nuevo diccionario  
elif opcion == '2':
    print('''
    ===============================
    TOTAL DE ENERGIA DADA A CADA
       CIUDAD POR CADA PLANTA
               CIUDADES
    Guayaquil
    Quito
    Loja
    Ambato
    Tena
    Nueva loja
    ===============================
    '''),

    n_ciudad2 = input('Ingrese el nombre de la ciudad: ')

    if n_ciudad2 == 'Guayaquil':
        print('Total de MWh, Coca Codo Sinclair: ', tot_coca_codo_g, 'MWh')
        print('Total de MWh, Sopladora:', tot_sopladora_g, 'MWh')
    elif n_ciudad2 == 'Quito':
        print('Total de MWh, Coca Codo Sinclair: ', tot_coca_codo_q, 'MWh')
        print('Total de MWh, Sopladora:', tot_sopladora_q, 'MWh')
    elif n_ciudad2 == 'Loja':
        print('Total de MWh, Sopladora:', tot_sopladora_l, 'MWh')
    else:
        print('Ninguna planta otorga energía a la ciudad seleccionada')
    print()

    exit


#3. Solicite el nombre de una región al usuario y presente cuento dinero ha recaudado la
#región
elif opcion == '3':
    print('''
    ===============================
          DINERO RECAUDADO 
              REGIONES
    Costa
    Sierra
    Oriente
    ===============================
    '''),

    n_region = input('Ingrese el nombre de la Región: ')

    if n_region == 'Costa':
        print('Total recaudado en la Región Costa: ', Costa, '$')
    elif n_region == 'Sierra':
        print('Total recaudado en la Región Sierra: ', Sierra, '$')
    elif n_region == 'Oriente':
        print(Oriente)
    else:
        print("Digite correctamente la primera letra en mayúscula")
    exit