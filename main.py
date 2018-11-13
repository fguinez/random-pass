import random
import string

def number_characters(message=False):
    if message:
        print(message)
    num = input('Ingresa el número de caracteres: ')
    if num.isnumeric():
        return int(num)
    return number_characters("Debes ingresar un número, intenta nuevamente.")

def isTrue(param):
    l = ['si', 'true', 'yes', 's', 't', 'verdadero', 'correcto', 'afirmativo']
    if param.lower() in l:
        return True
    return False

current_number = number_characters()
minus = input('¿Incluye minúsculas?: ')
mayus = input('¿Incluye mayúsculas?: ')
nums = input('¿Incluye números?: ')
spec = input('¿Incluye caracteres especiales?: ')

randoms = []

if isTrue(minus):
    randoms.append('minus')
if isTrue(mayus):
    randoms.append('mayus')
if isTrue(nums):
    randoms.append('nums')
if isTrue(spec):
    randoms.append('spec')

op = 'N'
while op != 'S':
    new_pass = ''
    if op == 'N':
        for _ in range(current_number):
            option = random.choice(randoms)
            if option == 'minus':
                new_pass += random.choice(string.ascii_letters).lower()
            elif option == 'mayus':
                new_pass += random.choice(string.ascii_letters).upper()
            elif option == 'nums':
                new_pass += str(random.randint(0, 9))
            elif option == 'spec':
                new_pass += random.choice(['-', '.', '_'])
    elif op == 'R':
        current_number = number_characters()
        minus = input('¿Incluye minúsculas?: ')
        mayus = input('¿Incluye mayúsculas?: ')
        nums = input('¿Incluye números?: ')
        spec = input('¿Incluye caracteres especiales?: ')
        if isTrue(minus):
            randoms.append('minus')
        if isTrue(mayus):
            randoms.append('mayus')
        if isTrue(nums):
            randoms.append('nums')
        if isTrue(spec):
            randoms.append('spec')
        op = 'N'
        continue
    else:
        print('Opción inválida. Intenta nuevamente.')
    print('Tu contraseña es: {}'.format(new_pass))
    print('----   (N) Nueva combinación        ----')
    print('----   (R) Reestablecer variables   ----')
    print('----   (S) Salir                    ----')
    op = input('¿Qué deseas hacer?: ').upper()
