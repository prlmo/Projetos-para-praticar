base = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]
valores = []
dias = []
valor_szero = []
vdias_maior_media = []
dias_maior = []
for posicao in base:
	valores.append(posicao['valor'])
	dias.append(posicao['dia'])
for posicao in base:
	if posicao['valor'] > 0:
		valor_szero.append(posicao['valor'])
media = sum(valor_szero) / len(valor_szero)
for posicao in base:
	if posicao['valor'] > media:
		vdias_maior_media.append(posicao['valor'])
valor_max = max(valores)
dia_max = valores.index(valor_max)
valor_min = min(valor_szero)
dia_min = valores.index(valor_min)

print(f'Dia {dias[dia_min]} foi o MENOR valor de faturamento ocorrido no mês, faturamento de: R${valor_min} ')
print(f'\nDia {dias[dia_max]} foi o MAIOR valor de faturamento ocorrido no mês, faturamento de: R${valor_max} ')
print(f'\nO número de dias com faturamento maior que a média foram no total {len(dias_maior)} dias\n')

j = 0
while j < len(valores)-1:
	if valores[j] in vdias_maior_media:
		print(f'dias e seus faturamentos\n'
			  f'dia: {dias[j]}, faturamento: R${valores[j]}\n')

		j += 1
	else:

		j += 1
