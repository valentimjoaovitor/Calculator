import os

# função de adição
def add(x, y):
    return x + y

# função de subtração
def sub(x, y):
    return x - y

# função de multiplicação
def mult(x, y):
    return x * y

# função de divisão
def div(x, y):
    if y == 0:
        return print("You can't divide with 0")
    return x / y


while True:
    
    print(f'------------CALCULATOR--------------')
    print(f"\nEnter 'add' for addition.")
    print("Enter 'sub' for subtraction.")
    print("Enter 'mult' for multiplication.")
    print("Enter 'div' for division.")
    print(f"Enter 'exit' to leave\t")

    user_input = input(f'\nEnter: ')

    if user_input == 'exit':
        print('Saindo do programa...')
        break

    if user_input in ('add', 'sub', 'mult', 'div'):
        valor1 = float(input('Enter the first number: '))
        valor2 = float(input('Enter the second number: '))

        if user_input == 'add':
            os.system('cls')
            print('result: ', add(valor1, valor2))
        elif user_input == 'sub':
            os.system('cls')
            print('result: ', sub(valor1, valor2))
        elif user_input == 'mult':
            os.system('cls')
            print('result: ', mult(valor1, valor2))
        elif user_input == 'div':
            os.system('cls')
            print(f'\nresult: ', div(valor1, valor2))


    else:
        print('invalid input')
        os.system('cls')