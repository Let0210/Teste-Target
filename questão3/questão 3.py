'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
      na linguagem que desejar, que calcule e retorne:
      • O menor valor de faturamento ocorrido em um dia do mês;
      • O maior valor de faturamento ocorrido em um dia do mês;
      • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

      IMPORTANTE:
      a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
      b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem
         ser ignorados no cálculo da média;'''

#-------------------------------------------------------

import json

data = 'questão3/dados.json'

def revenueMinAndMax(daily_rev):
    rev_min = float('inf')
    rev_max = float('-inf')


    for day in daily_rev:
        value = day["valor"]

        if value < rev_min:
            rev_min = value
        if value > rev_max:
            rev_max = value
    
    return f"Menor faturamento do mês: R$ {rev_min:.2f}\nMaior faturamento do mês: R$ {rev_max:.2f}"


def revenueMean(daily_rev):
    sum_rev = 0.0
    mean_rev = 0.0
    business_days = 0

    for day in daily_rev:
        value = day["valor"]

        if value> 0.0:
            business_days+= 1   #dias úteis
            sum_rev += value

    mean_rev = sum_rev/business_days

    return mean_rev  

def daysRevHigherMean(daily_rev, mean_rev):
     
    days = 0
     
    for day in daily_rev:
        value = day["valor"]

        if value>mean_rev:
            days += 1

    return days        


try:
    with open(data, 'r', encoding='utf-8') as arq:
        daily_rev = json.load(arq)

        print(revenueMinAndMax(daily_rev))
        print()
        print(f"Faturamento médio do mês: R$ {revenueMean(daily_rev):.2f}\n")
        print(f"Qtd. de dias em que o faturamento diário foi maior que o faturamento médio mensal: {daysRevHigherMean(daily_rev, revenueMean(daily_rev))}\n")

        

except Exception as e:
    print(f"Ocorreu o seguinte erro: {e}")

