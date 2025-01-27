emailCadastrado = {
    'admin': 'admin'
}

while True:
    print("\n")
    print("==" * 50)
    print(f"{' ':<40}MENU DE LOGIN")
    print("==" * 50)
    print("""
    [ 1 ] | Entrar
    [ 2 ] | Cadastrar
    [ 3 ] | Redefinir Senha
    [ 4 ] | Excluir Cadastro
    [ 5 ] | Sair
    """)
    print("==" * 50)
    menu = input(">> Insira o Número da Opção Desejada ( Ex: 1 ): ").strip()
    
    if menu not in ("1", "2", "3", "4", "5"):
        input(f"[ ! ] Opção Inválida! Pressione ENTER e Tente Novamente.")
    
    # Fazer Login
    elif menu == "1":
        print("\n")
        print("--" * 50)
        print(f"{' ':<40}FAZER LOGIN")
        print("--" * 50)
        print("Pressione 0 caso deseja Sair.\n")

        sair = False
        contagem = 3
        while True:
            email = input("-> Insira seu Email: ").strip()
            if email == "0":
                break
            elif email not in emailCadastrado:
                print(f"[ ! ] Email Inválido! Tente Novamente.\n")
            else:
                while True:
                    if contagem < 0:
                        input("[ X ] Muitas Tentativas! Pressione ENTER e Tente Novamente mais Tarde.")
                        sair = True
                        break
                    else:
                        senha = input("-> Insira sua Senha: ").strip()
                        if senha == emailCadastrado[email]:
                            input("\n[ ✔ ] Login Realizado com Sucesso! Pressione ENTER para Continuar.")
                            sair = True
                            break
                        else:
                            print(f"[ ! ] Senha Inválida! Você ainda tem {contagem} Tentativas.\n")
                            contagem -= 1
            if sair:
                break
    
    # Cadastrar novo Email
    elif menu == "2":
        print("\n")
        print("--" * 50)
        print(f"{' ':<40}CADASTRAR EMAIL")
        print("--" * 50)
        print("Pressione 0 caso deseja Sair.\n")

        sair = False
        while True:
            email = input("-> Insira seu Email: ").strip()
            if email == "0":
                break
            elif email in emailCadastrado:
                print("[ ! ] Email já Cadastrado! Insira outro Email.\n")
            elif ("@" in email) and ("." in email) and (email.index("@") < email.rindex(".")):
                while True:
                    senha = input("-> Crie sua Senha: ")
                    if senha.count(" ") > 0:
                        print("[ ! ] Senha Inválida! Sua Senha não pode haver Espaços.\n")
                    elif len(senha) < 5:
                        print("[ ! ] Senha Inválida! Sua Senha deve conter no Mínimo 5 Caracteres.\n")
                    else:
                        while True:
                            confirmacao = input("-> Confirme a sua Senha: ").strip()
                            if senha == confirmacao:
                                emailCadastrado[email] = senha
                                sair = True
                                input("\n[ ✔ ] Cadastro Realizado com Sucesso! Pressione ENTER.")
                                break
                            else:
                                print("[ ! ] A Senha está Diferente! Tente Novamente.\n")
                    if sair:
                        break
            else:
                print("[ ! ] Email Inválido! Tente Novamente.\n")
            if sair:
                break

    # Redefinir Senha
    elif menu == "3":
        print("\n")
        print("--" * 50)
        print(f"{' ':<40}REDEFINIR SENHA")
        print("--" * 50)
        print("Pressione 0 caso deseja Sair.\n")

        sair = False
        contagem = 3
        while True:
            email = input("-> Insira seu Email: ").strip()
            if email == "0":
                break
            elif email not in emailCadastrado:
                print(f"[ ! ] Email Inválido! Tente Novamente.\n")
            else:
                while True:
                    if contagem < 0:
                        input("[ X ] Muitas Tentativas! Pressione ENTER e Tente Novamente mais Tarde.")
                        sair = True
                        break
                    else:
                        senha = input("-> Insira sua Senha: ").strip()
                        if senha == emailCadastrado[email]:
                            print("\n--- MUDAR SENHA ---")
                            while True:
                                novaSenha = input("-> Insira sua Nova Senha: ")
                                if novaSenha.count(" ") > 0:
                                    print("[ ! ] Senha Inválida! Sua Senha não pode haver Espaços.\n")
                                elif len(novaSenha) < 5:
                                    print("[ ! ] Senha Inválida! Sua Senha deve conter no Mínimo 5 Caracteres.\n")
                                elif novaSenha == senha:
                                    print("[ ! ] A Senha permanece Igual! Faça alguma Alteração.\n")
                                else:
                                    while True:
                                        confirmacao = input("-> Confirme a sua Nova Senha: ").strip()
                                        if novaSenha == confirmacao:
                                            emailCadastrado[email] = novaSenha
                                            sair = True
                                            input("\n[ ✔ ] Senha Alterada com Sucesso! Pressione ENTER para Sair.")
                                            break
                                        else:
                                            print("[ ! ] A Senha está Diferente! Tente Novamente.\n")
                                if sair:
                                    break    
                        else:
                            print(f"[ ! ] Senha Inválida! Você ainda tem {contagem} Tentativas.\n")
                            contagem -= 1
                    if sair:
                        break
            if sair:
                break
    
    # Excluir Cadastro
    elif menu == "4":
        print("\n")
        print("--" * 50)
        print(f"{' ':<40}EXCLUIR CADASTRO")
        print("--" * 50)
        print("Pressione 0 caso deseja Sair.\n")

        sair = False
        contagem = 3
        while True:
            email = input("-> Insira seu Email: ").strip()
            if email == "0":
                break
            elif email not in emailCadastrado:
                print(f"[ ! ] Email Inválido! Tente Novamente.\n")
            else:
                while True:
                    if contagem < 0:
                        input("[ X ] Muitas Tentativas! Pressione ENTER e Tente Novamente mais Tarde.")
                        sair = True
                        break
                    else:
                        senha = input("-> Insira sua Senha: ").strip()
                        if senha == emailCadastrado[email]:
                            print("\n--- DESEJA MESMO EXCLUIR SEU CADASTRO? ---")
                            while True:
                                decisao = input("( S / N ): ").upper()
                                if decisao not in ("S", "N"):
                                    print("[ ! ] Opção Inválida! Insira S ou N.\n")
                                elif decisao == "S":
                                    del emailCadastrado[email]
                                    input("\n[ ✔ ] Cadastro Excluido com Sucesso! Pressione ENTER para Sair.")
                                    sair = True
                                    break
                                elif decisao == "N":
                                    input("\n[ ✔ ] Exclusão de Cadastro cancelada! Pressione ENTER para Sair.")
                                    sair = True
                                    break
                            if sair:
                                break
                        else:
                            print(f"[ ! ] Senha Inválida! Você ainda tem {contagem} Tentativas.\n")
                            contagem -= 1
            if sair:
                break

    # Encerrar Programa
    elif menu == "5":
        print("\n[ ✔ ] Programa Encerrado.\n")
        break