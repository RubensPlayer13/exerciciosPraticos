'''Esta é uma calculadora simples que suporta as seguintes operações:
- Soma
- Subtração
- Multiplicação
- Divisão
- Potência'''
import math


def calcular(operacao: str, num1: float, num2: float) -> float | str:
    '''Calcula o resultado da operação desejada.'''
    operacoes = {
        'soma': lambda a, b: a + b,
        'subtracao': lambda a, b: a - b,
        'multiplicacao': lambda a, b: a * b,
        'divisao': lambda a, b: a / b if b != 0 else "Erro: Divisão por zero",
        'potencia': math.pow,
        'raiz': lambda a, b: math.sqrt(a) if b == 2 else a ** (1/b)
    }
    return operacoes.get(operacao, "Operação inválida")(num1, num2)


while True:
    print("""
Calculadora Simples
Operações disponíveis:
    soma, subtracao,
    multiplicacao, divisao,
    potencia,
    raiz (para raiz quadrada, use o segundo numero como 2; para outras raízes,
    use o índice da raiz como segundo número)
""")
    escolha = input("Digite a operação desejada: ")
    number1 = float(input("Digite o primeiro número: "))
    number2 = float(input("Digite o segundo número: "))
    resultado = calcular(escolha, number1, number2)
    print(
        f"O resultado da {escolha} entre {number1} e {number2} é: {resultado}")
    continuar = input("\nDeseja realizar outra operação? (s/n): ").lower()
    if continuar != 's':
        break
