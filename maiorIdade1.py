

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade: "))
"""
#  Primeiro exemplo:
if idade >= MAIOR_IDADE:
    print('Voê é maior de idade, pode tirar a CNH.')

if idade < MAIOR_IDADE:
    print('Ainda não pode tirar a CNH.21')


# Segundo exemplo:
if idade >= MAIOR_IDADE:
    print('Voê é maior de idade, pode tirar a CNH.')

else:
    print('Ainda não pode tirar a CNH.21')z
"""
#  Terceiro exemplo:
if idade >= MAIOR_IDADE:
    print('Você é maior de idade, poderá fazer o treinamento e tirar a CNH.')
elif idade == IDADE_ESPECIAL:
    print('Poderá fazer as aulas teóricas.')
else:
    print("Não poderá realizar nenhum dos treinamentos no momento, devida a sua idade! ")