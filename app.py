import os

restauranteList = [
    {'name': "Piazza", 'category': 'Italian', 'is_active': False},
    {'name': "Suchi", 'category': 'Japonese', 'is_active': True},
    {'name': "Tacos", 'category': 'Mexican', 'is_active': False},
    {'name': "Coxinhas", 'category': 'Brazilian', 'is_active': True},
]

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

def restart_app():
    input("\nDigite uma nova tecla para iniciar novamente ")
    os.system("clear")
    main()

def show_subtitle(text):
    os.system("clear")
    print(text)
    print()

def exit_program():
    show_subtitle("Encerrando programa!")

def invalid_option():
    print("Operacao inválida! \n")
    restart_app()

def create_new_restaurant():
    show_subtitle("Adicionando novo restaurante!")
    
    restaurant_name = input("Digite o nome do novo restaurante: ")
    restaurant_category = input(f"Digite a categoria do restaurante {restaurant_name}: ")
    
    restaurant_data = {'name': restaurant_name, 'category': restaurant_category, 'is_active': False}
    restauranteList.append(restaurant_data)
    print(f"Novo restaurante: {restaurant_name} - cadastrado com sucesso!")
    restart_app()

def show_restaurante_list():
    show_subtitle("Listagem dos restaurantes cadastrados!")

    for restaurant in restauranteList:
        name = restaurant['name']
        category = restaurant['category']
        is_active = restaurant['is_active']

        print(f'. {name} - {category} - {is_active}')

    restart_app()

def choice_option():
    try:
        choiced_option = int(input('Escolha uma opção: '))

        if choiced_option == 1:
            create_new_restaurant()
        elif choiced_option == 2:
            show_restaurante_list()
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

