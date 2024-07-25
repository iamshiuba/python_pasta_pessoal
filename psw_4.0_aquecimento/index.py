nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media < 6:
    posRec = float(input("Digite a sua nota da recuperação: "))

mediaInicial = 6

notaFinal = (nota1 + nota2 + nota3 + posRec) / 4 if media < 6 else media

if media >= 6:
    print("Aprovado!")
elif mediaInicial >= 5.5 and mediaInicial < 6 and nota4 < 6.5:
    print("Recuperação!")
elif mediaInicial <= 5.5 and mediaInicial < 6 and nota4 < 9:
    print("Recuperação mediante a risco de reprovação por insuficiência!")
elif notaFinal >= mediaInicial:
    print("O resultado da recuperação foi positivo! Aprovado!")
else:
    print("O resultado da recuperação foi negativo! Reprovado!")

if media >= 6:
    print(f"Sua nota global foi: {nota1 + nota2 + nota3 + nota4}, média: {media}")
elif notaFinal >= mediaInicial:
    print(f"Sua nota global foi: {nota1 + nota2 + nota3 + posRec}, média: {notaFinal}")
else:
    print(f"Sua nota global foi: {nota1 + nota2 + nota3 + posRec}, média: {notaFinal}")
