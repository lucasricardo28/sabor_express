import os

restauranteList = [
    {'name': "Piazza", 'category': 'Italian', 'is_active': False},
    {'name': "Suchi", 'category': 'Japonese', 'is_active': True},
    {'name': "Tacos", 'category': 'Mexican', 'is_active': False},
    {'name': "Coxinhas", 'category': 'Brazilian', 'is_active': True},
]

def show_program_name():
    ''' Visualizar nome da aplicação! '''
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
        \n""")


def show_options():
    ''' Mostrar o menu de opções da aplicação.'''
    print('1 - Cadastrar restaurante!')
    print('2 - Listar restaurante!')
    print('3 - Alternar estado do restaurante!')
    print('4 - Sair \n')

def restart_app():
    ''' Comando para reiniciar a aplicação.'''
    input("\nDigite uma nova tecla para iniciar novamente ")
    os.system("clear")
    main()

def show_subtitle(text):
    '''Mostrar subtitulo ao selecionar menu.'''
    os.system("clear")
    linha = '*' * (len(text) + 2)
    print(linha)
    print(text)
    print(linha)
    print()

def exit_program():
    '''Encerramento do programa!'''
    show_subtitle("Encerrando programa!")

def invalid_option():
    ''' Mensagem para o usuario que informou dado errado!'''
    print("Operacao inválida! \n")
    restart_app()

def create_new_restaurant():
    '''
    Criando um novo restaurante 

    Inputs:
    - Nome do restaurante 
    - Categoria do restaurante 

    Outputs:
    - Adicionando novo restaurante na lista de restaurantes
    '''
    show_subtitle("Adicionando novo restaurante!")
    
    restaurant_name = input("Digite o nome do novo restaurante: ")
    restaurant_category = input(f"Digite a categoria do restaurante {restaurant_name}: ")
    
    restaurant_data = {'name': restaurant_name, 'category': restaurant_category, 'is_active': False}
    restauranteList.append(restaurant_data)
    print(f"Novo restaurante: {restaurant_name} - cadastrado com sucesso!")
    restart_app()

def show_restaurante_list():
    ''' Mostrando lista dos restaurantes cadastrados!'''
    show_subtitle("Listagem dos restaurantes cadastrados!")

    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status ')

    for restaurant in restauranteList:
        name = restaurant['name']
        category = restaurant['category']
        is_active = 'Ativo' if restaurant['is_active'] else 'Desativado'

        print(f'- {name.ljust(20)} | {category.ljust(20)} | {is_active.ljust(20)}')

    restart_app()

def update_status_restaurant():
    '''
    Atualizando status de um restaurante
    
    Inputs:
    - Nome do restaurante para alterar status 
    '''
    show_subtitle("Editando status do restaurante!")

    restaurante_to_find = input("Informe o nome do restaurante: ")
    has_found_restaurant = False

    for restaurant in restauranteList:
        if restaurant['name']  == restaurante_to_find:
            has_found_restaurant = True
            restaurant['is_active'] = not restaurant['is_active']
            message = f' O restaurante : {restaurant['name']} foi Ativado com sucesso!' if restaurant['is_active'] else f'O restaurante : {restaurant['name']} foi desativado com sucesso!'
            print(message)
    if not has_found_restaurant:
        print('Nenhum restaurante encontrado!')

    restart_app()

def choice_option():
    ''' Escolhendo opcao para executar uma acao. '''
    try:
        choiced_option = int(input('Escolha uma opção: '))

        if choiced_option == 1:
            create_new_restaurant()
        elif choiced_option == 2:
            show_restaurante_list()
        elif choiced_option == 3:
            update_status_restaurant()
        elif choiced_option == 4:
            exit_program()
        else :
            invalid_option()
    except:
        invalid_option()

def main():
    ''' Funcao princiapl do programa!'''
    show_program_name()
    show_options()
    choice_option()

if __name__ == '__main__':
    main()

