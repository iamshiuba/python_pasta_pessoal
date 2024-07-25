def calcular_media(notas):
    return sum(notas) / len(notas)

# Coleta das 4 notas iniciais
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

# Cálculo da média inicial
notas = [nota1, nota2, nota3, nota4]
media = calcular_media(notas)

# Verificação da necessidade de recuperação
if media < 6:
    if media >= 5.5 and nota4 < 6.5:
        print("Recuperação!")
    elif media < 5.5 and nota4 < 9:
        print("Recuperação mediante a risco de reprovação por insuficiência!")
    
    posRec = float(input("Digite a sua nota da recuperação: "))
    notas[3] = posRec  # Substitui a quarta nota pela nota de recuperação
    notaFinal = calcular_media(notas)
else:
    notaFinal = media

# Determinação do status do aluno
if notaFinal >= 6:
    print("Aprovado!")
else:
    print("O resultado da recuperação foi negativo! Reprovado!")

# Impressão das notas e médias
if media >= 6:
    print(f"Sua nota global foi: {sum([nota1, nota2, nota3, nota4])}, média: {media:.2f}")
else:
    print(f"Sua nota global foi: {sum(notas)}, média: {notaFinal:.2f}")