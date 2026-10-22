def exibir_menu():
    print("\n===== CADASTRO DE ALUNOS =====")
    print("1 - Adicionar aluno")
    print("2 - Atualizar notas")
    print("3 - Remover aluno")
    print("4 - Exibir alunos e notas")
    print("5 - Exibir médias")
    print("0 - Sair")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip().title()
        if texto:
            return texto
        print("Erro: O campo não pode ficar em branco.")


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0.0 <= nota <= 10.0:
                return nota
            print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um número real válido.")


def ler_quatro_notas():
    notas = []
    for i in range(1, 5):
        nota = ler_nota(f"Digite a nota N{i}: ")
        notas.append(nota)
    return notas


def adicionar_aluno(alunos, nome, notas):
    if nome in alunos:
        print(f"Aluno(a) '{nome}' já está cadastrado(a). Sugerimos usar a opção de atualizar notas.")
        return False
    alunos[nome] = notas
    print(f"Aluno(a) '{nome}' cadastrado(a) com sucesso.")
    return True


def atualizar_notas(alunos, nome, notas):
    if nome in alunos:
        alunos[nome] = notas
        print(f"Notas do aluno(a) '{nome}' atualizadas com sucesso.")
        return True
    print(f"Aluno(a) '{nome}' não encontrado(a).")
    return False


def remover_aluno(alunos, nome):
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno(a) '{nome}' removido(a) com sucesso.")
        return True
    print(f"Aluno(a) '{nome}' não encontrado(a).")
    return False


def calcular_media(notas):
    return sum(notas) / len(notas)


def exibir_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    print("\n--- LISTA DE ALUNOS E NOTAS ---")
    for aluno, notas in alunos.items():
        print(f"- {aluno}: {notas}")


def exibir_medias(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado")
        return
    print("\n--- MÉDIAS DOS ALUNOS ---")
    for aluno, notas in alunos.items():
        media = calcular_media(notas)
        print(f"- {aluno}: Média = {media:.2f}")


def main():
    # Inicializado com o dicionário de testes sugerido
    alunos = {
        "Ana": [8.5, 7.0, 9.2, 6.8],
        "Carlos": [5.5, 6.0, 7.5, 8.0],
        "Mariana": [9.0, 8.5, 10.0, 9.8],
        "Lucas": [6.5, 7.2, 5.8, 6.9],
        "Fernanda": [7.8, 8.2, 7.0, 8.5]
    }

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_texto("Nome do aluno: ")
            notas = ler_quatro_notas()
            adicionar_aluno(alunos, nome, notas)
        elif opcao == "2":
            nome = ler_texto("Nome do aluno para atualizar: ")
            if nome in alunos:
                notas = ler_quatro_notas()
                atualizar_notas(alunos, nome, notas)
            else:
                print(f"Aluno(a) '{nome}' não encontrado(a).")
        elif opcao == "3":
            nome = ler_texto("Nome do aluno a remover: ")
            remover_aluno(alunos, nome)
        elif opcao == "4":
            exibir_alunos(alunos)
        elif opcao == "5":
            exibir_medias(alunos)
        elif opcao == "0":
            print("Saindo do sistema escolar...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
