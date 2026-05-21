import users_wrapper as api

rodando = True

while rodando:

    print("\n====== MENU ======")
    print("1 - Ver usuários")
    print("2 - Buscar usuário")
    print("3 - Adicionar usuário")
    print("4 - Editar usuário")
    print("5 - Remover usuário")
    print("0 - Encerrar")

    escolha = input("Escolha uma opção: ")

    # LISTAR
    if escolha == "1":

        lista_usuarios = api.list()

        if lista_usuarios:

            print("\n--- LISTA DE USUÁRIOS ---")

            for pessoa in lista_usuarios:
                print(f"{pessoa['id']} | {pessoa['name']}")

        else:
            print("Não foi possível carregar os usuários.")

    # DETALHAR
    elif escolha == "2":

        try:
            codigo = int(input("Informe o ID: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        usuario = api.read(codigo)

        if usuario:

            print("\n===== DADOS DO USUÁRIO =====")

            print(f"Nome: {usuario['name']}")
            print(f"Usuário: {usuario['username']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Telefone: {usuario['phone']}")
            print(f"Site: {usuario['website']}")

            endereco = usuario["address"]

            print("\n--- ENDEREÇO ---")
            print(f"Rua: {endereco['street']}")
            print(f"Cidade: {endereco['city']}")
            print(f"CEP: {endereco['zipcode']}")

            empresa = usuario["company"]

            print("\n--- EMPRESA ---")
            print(f"Empresa: {empresa['name']}")

        else:
            print("Usuário não encontrado.")

    # CRIAR
    elif escolha == "3":

        novo_usuario = {
            "name": input("Nome: "),
            "username": input("Username: "),
            "email": input("Email: "),
            "phone": input("Telefone: "),
            "website": input("Website: "),

            "address": {
                "street": input("Rua: "),
                "suite": input("Suite: "),
                "city": input("Cidade: "),
                "zipcode": input("CEP: "),

                "geo": {
                    "lat": input("Latitude: "),
                    "lng": input("Longitude: ")
                }
            },

            "company": {
                "name": input("Empresa: "),
                "catchPhrase": input("Slogan: "),
                "bs": input("BS: ")
            }
        }

        resultado = api.create(novo_usuario)

        if resultado:
            print("Usuário cadastrado.")
        else:
            print("Erro ao cadastrar.")

    # ATUALIZAR
    elif escolha == "4":

        try:
            codigo = int(input("ID do usuário: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        dados_atualizados = {
            "name": input("Novo nome: "),
            "username": input("Novo username: "),
            "email": input("Novo email: "),
            "phone": input("Novo telefone: "),
            "website": input("Novo website: "),

            "address": {
                "street": input("Rua: "),
                "suite": input("Suite: "),
                "city": input("Cidade: "),
                "zipcode": input("CEP: "),

                "geo": {
                    "lat": input("Latitude: "),
                    "lng": input("Longitude: ")
                }
            },

            "company": {
                "name": input("Empresa: "),
                "catchPhrase": input("Slogan: "),
                "bs": input("BS: ")
            }
        }

        alteracao = api.update(codigo, dados_atualizados)

        if alteracao:
            print("Usuário atualizado.")
        else:
            print("Erro ao atualizar.")

    # DELETAR
    elif escolha == "5":

        try:
            codigo = int(input("Informe o ID: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        apagar = api.delete(codigo)

        if apagar:
            print("Usuário removido.")
        else:
            print("Erro ao remover usuário.")

    # SAIR
    elif escolha == "0":

        print("Sistema encerrado.")
        rodando = False

    else:
        print("Opção inválida.")