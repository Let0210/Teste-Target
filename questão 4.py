'''4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
      • SP - R$67.836,43
      • RJ - R$36.678,66
      • MG - R$29.229,88
      • ES - R$27.165,48
      • Outros - R$19.849,53

      Escreva um programa na linguagem que desejar onde calcule o percentual de
      representação que cada estado teve dentro do valor total mensal da distribuidora'''

#-------------------------------------------------------

import matplotlib.pyplot as plt

data = [
	{
		"estado": "SP",
		"fatur_mensal": 67836.43
	},
	{
		"estado": "RJ",
		"fatur_mensal": 36678.66
	},
	{
		"estado": "MG",
		"fatur_mensal": 29229.88
	},
	{
		"estado": "ES",
		"fatur_mensal": 27165.48
	},
	{
		"estado": "Outros",
		"fatur_mensal": 19849.53
	}
]

revenue_total = sum(uf['fatur_mensal'] for uf in data)

for uf in data:
    uf['percentual'] = (uf["fatur_mensal"]/revenue_total) * 100


slices = [uf['estado'] for uf in data]
percentages = [uf['percentual'] for uf in data]

plt.figure(figsize=(8,8))
plt.pie(percentages, labels=slices, autopct='%1.2f%%')
plt.title('Faturamento mensal por estado em %')
plt.show()
