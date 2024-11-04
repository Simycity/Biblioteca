# Cadastro dos livros;
print("Cadastro de 5 livros")

# Variável de armazenamento do livro 1;
titulo_1 = ""
autor_1 = ""
ano_1 = ""

print("Cadastro do Livro 1: ")
titulo_1 = input("Título: ")
autor_1 = input("Autor: ")
ano_1 = input("Ano de Publicação: ")

# Variável de armazenamento do livro 2;
titulo_2 = ""
autor_2 = ""
ano_2 = ""

print("Cadastro do Livro 2: ")
titulo_2 = input("Título: ")
autor_2 = input("Autor: ")
ano_2 = input("Ano de Publicação: ")

# Variável de armazenamento do livro 3;
titulo_3 = ""
autor_3 = ""
ano_3 = ""

print("Cadastro do Livro 3: ")
titulo_3 = input("Título: ")
autor_3 = input("Autor: ")
ano_3 = input("Ano de Publicação: ")

# Variável de armazenamento do livro 4;
titulo_4 = ""
autor_4 = ""
ano_4 = ""

print("Cadastro do Livro 4: ")
titulo_4 = input("Título: ")
autor_4 = input("Autor: ")
ano_4 = input("Ano de Publicação: ")

# Variável de armazenamento do livro 5;
titulo_5 = ""
autor_5 = ""
ano_5 = ""

print("Cadastro do Livro 5: ")
titulo_5 = input("Título: ")
autor_5 = input("Autor: ")
ano_5 = input("Ano de Publicação: ")

# while declarado para entrar no looping com o menu de opções;
while True:
    print("\nSistema de Gerenciamento de Biblioteca")
    print("1. Listar Livros Cadastrados")
    print("2. Consultar Livros Disponíveis")
    print("3. Empréstimo de Livro")
    print("4. Devolução de Livro")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")

    # Listar livros cadastrados;
    if opcao == "1":
        print("Lista de Livros Cadastrados:")
        if titulo_1:
            print(f"Título: {titulo_1}")
            print(f"Autor: {autor_1}")
            print(f"Ano: {ano_1}")

        if titulo_2:
            print(f"Título: {titulo_2}")
            print(f"Autor: {autor_2}")
            print(f"Ano: {ano_2}")

        if titulo_3:
            print(f"Título: {titulo_3}")
            print(f"Autor: {autor_3}")
            print(f"Ano: {ano_3}")
        if titulo_4:
            print(f"Título: {titulo_4}")
            print(f"Autor: {autor_4}")
            print(f"Ano: {ano_4}")

        if titulo_5:
            print(f"Título: {titulo_5}")
            print(f"Autor: {autor_5}")
            print(f"Ano: {ano_5}")

    #Consulta de livros disponíveis;
    elif opcao == "2":
        print("Livros Disponíveis:")

        # Disponibilidade do livro 1;
        disponivel_1 = "Disponível"
        if disponivel_1 == "Disponível":
            print(f"Título: {titulo_1}")
            print(f"Autor: {autor_1}")
            print(f"Ano: {ano_1}")

            # Disponibilidade do livro 2;
            disponivel_2 = "Disponivel"
        if disponivel_2 == "Disponível":
            print(f"Título: {titulo_2}")
            print(f"Autor: {autor_2}")
            print(f"Ano: {ano_2}")

            # Disponibilidade do livro 3;
            disponivel_3 = "Disponivel"
        if disponivel_3 == "Disponível":
            print(f"Título: {titulo_3}")
            print(f"Autor: {autor_3}")
            print(f"Ano: {ano_3}")

            # Disponibilidade do livro 4;
            disponivel_4 = "Disponível" 
        if disponivel_4 == "Disponível":
            print(f"Título: {titulo_4}")
            print(f"Autor: {autor_4}")
            print(f"Ano: {ano_4}")

            # Disponibilidade do livro 5;
            disponivel_5 = "Disponível"
        if disponivel_5 == "Disponível":
            print(f"Título: {titulo_5}")
            print(f"Autor: {autor_5}")
            print(f"Ano: {ano_5}")

    #Empréstimo de Livro;
    elif opcao == "3":
        titulo = input("Digite o título do livro para empréstimo: ")
       
        # Verificação para saber se o livro foi emprestado ou não;
        if titulo == titulo_1 and disponivel_1 == "Disponível":
            disponivel_1 = "Emprestado"
            print(f"Título: {titulo_1}, emprestado com sucesso.")

        elif titulo == titulo_2 and disponivel_2 == "Disponível":
            disponivel_2 = "Emprestado"
            print(f"Título: {titulo_2}, emprestado com sucesso.")

        elif titulo == titulo_3 and disponivel_3 == "Disponível":
            disponivel_3 = "Emprestado"
            print(f"Título: {titulo_3}, emprestado com sucesso.")
        
        elif titulo == titulo_4 and disponivel_4 == "Disponível":
            disponivel_4 = "Emprestado"
            print(f"Título: {titulo_4}, emprestado com sucesso.")

        elif titulo == titulo_5 and disponivel_5 == "Disponível":
            disponivel_5 = "Emprestado"
            print(f"Título: {titulo_5}, emprestado com sucesso." )

        else:
            print("Livro indisponível ou não encontrado")

    # Data de Devolução do livro;
    elif opcao == "4":

        titulo = input("Digite o título do livro para devolução: ")
        
        if titulo == titulo_1 and disponivel_1 == "Emprestado":
            disponivel1 = "Disponível"
            print(f"Título: {titulo_1}, foi devolvido com sucesso." )

        elif titulo == titulo_2 and disponivel_2 == "Emprestado":
            disponivel2 = "Disponível"
            print(f"Título: {titulo_2}, foi devolvido com sucesso.")

        elif titulo == titulo_3 and disponivel_3 == "Emprestado":
            disponivel3 = "Disponível"
            print(f"Título: {titulo_3}, foi devolvido com sucesso.")

        elif titulo == titulo_4 and disponivel_4 == "Emprestado":
            disponivel_4 = "Disponível"
            print(f"O título: {titulo_4}, foi devolvido com sucesso.")

        elif titulo == titulo_5 and disponivel_5 == "Emprestado":
            disponivel_5 = "Disponível"
            print(f"Título: {titulo_5}, foi devolvido com sucesso.")

        else:
            print("Livro não encontrado no catálogo.")
    
    #Saída de sistema.
    elif opcao == "5":
        print("Saindo do sistema de biblioteca.")
        break
    else:
        print("Opção inválida. Tente novamente.")



