from colorama import init, Fore, Style
import matplotlib.pyplot as plt

# Inicializa o colorama (necessário para funcionar em Windows)
init(autoreset=True)

# Lista de alunos em recuperação
recuperacao = [
    "ANA JULIA LIBORIO SOUZA",
    "BEATRIZ VICTORIA CARIAS DA SILVA",
    "CAIO VICTOR DA COSTA SANTOS",
    "GABRIEL ALVES MENDES DA SILVA",
    "GUILHERME DOS SANTOS DA SILVA",
    "ISABELLY APARECIDA DA SILVA",
    "KAUAN REGIS DOS SANTOS NASCIMENTO",
    "MIGUEL FERNANDES OLIVEIRA",
    "MURILO MATIAS DOS SANTOS",
    "ANA GABRIELE DA SILVA NEIVA DE LIMA",
    "BIANCA FERREIRA DOS SANTOS",
    "CLAUDIO DIAS DE OLIVEIRA JUNIOR",
    "DAVID LUIS OLIVEIRA DE BARROS",
    "DOUGLAS DE MORAES LOPES DA SILVA",
    "ELAINE ROCHA COSTA",
    "EMILLY ARAUJO SANTOS",
    "GABRIEL RICARDO GONCALVES DA SILVA",
    "KELVIN XAVIER DE SOUZA",
    "LUCAS DE SOUZA GONCALVES",
    "FLAVIA EDUARDA DE OLIVEIRA SANTOS",
    "JULIANA SILVA"
]

# Função para validar o nome do aluno
def validar_nome(nome):
    nome_formatado = nome.strip().upper()
    if not nome_formatado or not any(c.isalpha() for c in nome_formatado):
        print(f"{Fore.RED}Nome inválido! Por favor, insira um nome válido.{Style.RESET_ALL}")
        return None
    return nome_formatado

# Função para solicitar as notas
def solicitar_notas():
    """Solicita as notas do aluno e retorna uma lista de valores válidos."""
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"{Fore.YELLOW}Digite a nota do {i}º bimestre (0 a 10): {Style.RESET_ALL}"))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um número entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")
    return notas

# Função para calcular soma e média das notas
def calcular_media(notas):
    """Calcula e retorna a soma e a média das notas."""
    if not notas:
        print(f"{Fore.RED}Erro: Lista de notas está vazia!{Style.RESET_ALL}")
        return 0, 0
    soma = sum(notas)
    media = soma / len(notas)
    return soma, media

# Função para exibir gráficos das notas com cores baseadas em desempenho
def exibir_grafico(notas):
    """Exibe um gráfico das notas de cada bimestre."""
    bimestres = ['1º', '2º', '3º', '4º']
    cores = []

    for nota in notas:
        if nota >= 8:
            cores.append('green')
        elif 5 <= nota < 8:
            cores.append('blue')
        else:
            cores.append('red')

    plt.bar(bimestres, notas, color=cores)
    plt.xlabel('Bimestres')
    plt.ylabel('Notas')
    plt.title('Desempenho Bimestral do Aluno')
    plt.ylim(0, 10)
    plt.show()

# Função para exibir o resultado
def exibir_resultado(nome, soma, media, notas):
    """Exibe o resultado do aluno com base nas notas e na lista de recuperação."""
    print(f"\n{Fore.CYAN}Soma das notas: {soma:.2f}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Média: {media:.2f}{Style.RESET_ALL}")

    # Feedback visual
    if nome in recuperacao:
        print(f"{Fore.PINK}⚠️ O aluno está na lista de recuperação. Precisa de um esforço extra! 💪{Style.RESET_ALL}")
    else:
        if soma >= 20:
            print(f"{Fore.GREEN}✔️ Parabéns, o aluno está aprovado! 🎉{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}❌ Infelizmente, o aluno está reprovado. 😔{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Dica: Revise os conteúdos dos bimestres para melhorar!{Style.RESET_ALL}")

    # Exibindo gráfico das notas
    exibir_grafico(notas)

# Função para revisar as notas
def revisar_notas(notas):
    """Permite ao aluno revisar suas notas e atualizar caso necessário."""
    print(f"{Fore.YELLOW}Você pode revisar as notas agora.{Style.RESET_ALL}")
    for i in range(4):
        while True:
            try:
                nova_nota = float(input(f"{Fore.CYAN}Digite a nova nota para o {i+1}º bimestre (atual: {notas[i]}): {Style.RESET_ALL}"))
                if 0 <= nova_nota <= 10:
                    notas[i] = nova_nota
                    break
                else:
                    print(f"{Fore.RED}A nota deve ser um número entre 0 e 10.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Entrada inválida. Digite um número.{Style.RESET_ALL}")
    return notas

# Função para gerar um relatório final
def gerar_relatorio(nome, soma, media, notas):
    """Gera um relatório simples com os dados do aluno."""
    print("\n--- RELATÓRIO FINAL ---")
    print(f"Aluno: {nome}")
    print(f"Notas: {', '.join([str(nota) for nota in notas])}")
    print(f"Soma das notas: {soma:.2f}")
    print(f"Média: {media:.2f}")
    print("-----------------------")

# Função principal
def verificar_aprovacao():
    """Função principal do programa."""
    print(f"{Fore.BLUE}Bem-vindo ao sistema de avaliação escolar!{Style.RESET_ALL}")
    nome = input(f"{Fore.YELLOW}Digite o nome completo do aluno: {Style.RESET_ALL}")
    nome_formatado = validar_nome(nome)

    if nome_formatado is None:
        return

    # Solicitar as notas e calcular a média
    notas = solicitar_notas()
    soma, media = calcular_media(notas)

    # Exibir resultado
    exibir_resultado(nome_formatado, soma, media, notas)

    # Perguntar se deseja revisar as notas
    revisar = input(f"{Fore.YELLOW}Deseja revisar as notas? (s/n): {Style.RESET_ALL}").strip().lower()
    if revisar == 's':
        notas = revisar_notas(notas)
        soma, media = calcular_media(notas)
        exibir_resultado(nome_formatado, soma, media, notas)

    # Gerar relatório final
    gerar_relatorio(nome_formatado, soma, media, notas)

# Executar o programa
if __name__ == "__main__":
    verificar_aprovacao()
