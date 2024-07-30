def calcular_media(notas):
    return sum(notas) / len(notas)


nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

notas = [nota1, nota2, nota3, nota4]
media = calcular_media(notas)

if media < 5:
    if media >= 4.5 and nota4 < 5.5:
        print("Recuperação!")
    elif media < 4.5 and nota4 < 8:
        print("Recuperação mediante a risco de reprovação por insuficiência!")

    posRec = float(input("Digite a sua nota da recuperação: "))
    notas[3] = posRec
    notaFinal = calcular_media(notas)
else:
    notaFinal = media

if notaFinal >= 5:
    print("Aprovado!")
else:
    print("O resultado da recuperação foi negativo! Reprovado!")

if media >= 5:
    print(f"Sua nota global foi: {sum(notas)}, média: {media:.2f}")
else:
    print(f"Sua nota global foi: {sum(notas)}, média: {notaFinal:.2f}")
