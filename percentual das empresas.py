SP0 = 67.83643
RJ1 = 36.67866
MG2 = 29.22988
ES3 = 27.16548
outros = 19.84953
soma = SP0 +RJ1 + MG2 + ES3 + outros
L = [67.83643, 36.67866, 29.22988, 27.16548]
L2 = ['SP', 'RJ', 'MG', 'ES']
i = 0
j = 0
while i < 4:
    x = 100 * L[i]
    print(f'Estado de {L2[j]} teve o persentual mensal de:{x/soma:.2f}%\n')
    j += 1
    i += 1
print(f'os Outros estados tiveram um percentual de {(100*outros)/soma:.2f}%')
print('\nEsse valores foram com Base no total de R$180.759,98 reais')