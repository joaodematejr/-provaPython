status = True

while True:
    print('Digite uma nota de 0 a 10:')
    note = int(input())
    if note >= 0 and note <= 10:
        break
    else:
        print('Nota invalida digite uma nota entre 0 e 10')

print("Parabens nota certa!")
