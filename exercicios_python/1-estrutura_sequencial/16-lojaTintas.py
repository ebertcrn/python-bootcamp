from math import ceil

def quantidade_latas(area):
    volume_lata = 54
    valor_lata = 80
    numero_latas = ceil(area / volume_lata)

    if area <= 54:
        print(f'Será necessária {numero_latas} lata de tinta.')
        print(f'O valor total será de R${valor_lata}.')
    else:
        print(f'Serão necessárias {numero_latas} latas de tinta.')
        print(f'O valor total será de R${valor_lata * numero_latas}.')

# teste
quantidade_latas(54)
quantidade_latas(1)
quantidade_latas(100)