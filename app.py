import os

restauranteList = []

def show_program_name():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        \n""")


def show_options():
    print('1 - Cadastrar restaurante!')
    print('2 - Listar restaurante!')
    print('3 - Ativar restaurante!')
    print('4 - Sair \n')

def exit_program():
    os.system('clear')
    print("Encerrando programa! \n")

def invalid_option():
    print("Operacao inválida! \n")
    input("Digito inválido, clique uma tecla para iniciar novamente!")
    os.system('clear')
    main()

def create_new_restaurant():
    os.system("clear")
    new_restaurant = input("Digite o nome do novo restaurante: ")
    restauranteList.append(new_restaurant)
    print(f"Novo restaurante {new_restaurant} cadastrado com sucesso! \n")
    input("Digite uma nova tecla para iniciar novamente")
    os.system("clear")
    main()

def choice_option():
    try:
        choiced_option = int(input('Escolha uma opção: '))

        if choiced_option == 1:
            create_new_restaurant()
        elif choiced_option == 2:
            print('Listar restaurantes')
        elif choiced_option == 3:
            print('Ativar restaurante')
        elif choiced_option == 4:
            exit_program()
        else :
            invalid_option()
    except:
        invalid_option()

def main():
    show_program_name()
    show_options()
    choice_option()

if __name__ == '__main__':
    main()

