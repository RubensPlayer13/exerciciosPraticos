"""Calculadora com histórico de operações.

Suporta:
- Soma
- Subtração
- Multiplicação
- Divisão
- Potência
- Raíz
"""
import math
import os
from datetime import datetime

# fixa o histórico na pasta onde o script está localizado
BASE_DIR = os.path.dirname(__file__)
HISTORY_FILE = os.path.join(BASE_DIR, 'historico.txt')


def calcular(operacao: str, num1: float, num2: float) -> float | str:
    """Calcula o resultado da operação desejada."""
    operacoes = {
        'soma': lambda a, b: a + b,
        'subtracao': lambda a, b: a - b,
        'multiplicacao': lambda a, b: a * b,
        'divisao': lambda a, b: (a / b if b != 0
                                 else "Erro: Divisão por zero"),
        'potencia': math.pow,
        'raiz': lambda a, b: (math.sqrt(a) if b == 2
                              else a ** (1 / b))
    }
    msg = "Operação inválida"
    return operacoes.get(operacao, msg)(num1, num2)


# variáveis iniciais
historico: list[str] = []


def carregar_historico(path: str) -> list[str]:
    """Carrega o histórico de um arquivo."""
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()
                if line.strip()]


def salvar_entrada(entrada: str, path: str) -> None:
    """Salva uma entrada no arquivo de histórico."""
    with open(path, 'a', encoding='utf-8') as f:
        f.write(entrada + '\n')


def limpar_historico(path: str) -> list[str]:
    """Limpa o histórico em memória e arquivo."""
    if os.path.exists(path):
        os.remove(path)
    return []


historico = carregar_historico(HISTORY_FILE)

while True:
    print("""Calculadora Simples
Operações disponíveis:
    soma, subtracao,
    multiplicacao, divisao,
    potencia,
    raiz (para raiz quadrada, use o segundo numero como 2; para outras raízes,
    use o índice da raiz como segundo número),
    historico (mostra o histórico de operações),
    limpar (limpa o histórico)
""")
    escolha = input("Digite a operação desejada: ").strip().lower()

    if escolha == 'historico':
        if not historico:
            print("Nenhuma operação no histórico.")
        else:
            print("Histórico de operações:")
            for i, entry in enumerate(historico, start=1):
                print(f"{i}. {entry}")
        continuar = (input("\nDeseja realizar outra operação? "
                           "(s/n): ").lower())
        if continuar != 's':
            break
        continue

    if escolha == 'limpar':
        MSG = "Tem certeza que deseja limpar todo o histórico? (s/n): "
        resposta = input(MSG).lower()
        if resposta == 's':
            historico = limpar_historico(HISTORY_FILE)
            print("Histórico limpo com sucesso!")
        else:
            print("Operação cancelada.")
        continuar = (input("\nDeseja realizar outra operação? "
                           "(s/n): ").lower())
        if continuar != 's':
            break
        continue

    try:
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida: por favor digite números.")
        continue

    resultado = calcular(escolha, number1, number2)
    print(f"O resultado da {escolha} entre {number1} e {number2} "
          f"é: {resultado}")

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ENTRADA = (f"[{timestamp}] {escolha} - {number1}, {number2} = "
               f"{resultado}")
    historico.append(ENTRADA)
    try:
        salvar_entrada(ENTRADA, HISTORY_FILE)
    except OSError as e:
        MSG = f"Aviso: não foi possível salvar o histórico: {e}"
        print(MSG)

    continuar = (input("\nDeseja realizar outra operação? "
                       "(s/n): ").lower())
    if continuar != 's':
        break
