N = int(input('Digite uma numero para a sequência de fibonacci: '))
while N <= 1:
    try:
        N = int(input('\nDigite um numero maior que 1: '))
        if N < 2:
            N = int(input('\nDigite um numero maior que 1 ou igual a 2: '))
    except:
        print('\nSó é possivel digitar numeros e inteiros.')
L = [0, 1, ]
for i in range(N-2):
    L.append(L[i] + L[i+1])
print(f'Sequencia fibonacci gerada : {L}')
if N in L:
    print(f'O valor {N} inserido, SIM, está na Sequência de Fibonacci')
else:
    print(f'O valor {N} inserido, NÃO, está na Sequência de Fibonacci')