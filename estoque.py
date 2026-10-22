def exibir_menu():
    print("\n===== ESTOQUE DA LOJA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Exibir estoque")
    print("0 - Sair")


def ler_quantidade(mensagem):
    while True:
        try:
            quantidade = int(input(mensagem))
            if quantidade >= 0:
                return quantidade
            print("Erro: A quantidade deve ser maior ou igual a zero.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip().title()
        if texto:
            return texto
        print("Erro: O campo não pode ficar em branco.")


def adicionar_produto(estoque, nome, quantidade):
    if nome in estoque:
        print(f"Produto '{nome}' já está cadastrado. Sugerimos usar a opção de atualizar.")
        return False
    estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado com sucesso.")
    return True


def remover_produto(estoque, nome):
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso.")
        return True
    print(f"Produto '{nome}' não encontrado.")
    return False


def atualizar_quantity(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada com sucesso.")
        return True
    print(f"Produto '{nome}' não encontrado.")
    return False


def exibir_estoque(estoque):
    if not estoque:
        print("Estoque vazio")
        return
    print("\n--- PRODUTOS EM ESTOQUE ---")
    for produto, qtd in estoque.items():
        print(f"- {produto}: {qtd} unidades")


def main():
    estoque = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_texto("Nome do produto: ")
            quantidade = ler_quantidade("Quantidade: ")
            adicionar_produto(estoque, nome, quantidade)
        elif opcao == "2":
            nome = ler_texto("Nome do produto a remover: ")
            remover_produto(estoque, nome)
        elif opcao == "3":
            nome = ler_texto("Nome do produto a atualizar: ")
            quantidade = ler_quantidade("Nova quantidade: ")
            atualizar_quantity(estoque, nome, quantidade)
        elif opcao == "4":
            exibir_estoque(estoque)
        elif opcao == "0":
            print("Saindo do sistema de estoque...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
