'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a
      soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa
      na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
      e retorne uma mensagem avisando se o número informado pertence ou não a sequência. '''

#-------------------------------------------------------

def fibonacciSequenceUntilNum(num):
    if num<1:
        return "O número informado precisa ser igual ou maior que 1"
    else:

        x = 0
        y = 1
        seq = [x, y]

        while y <= num:
            next_num =  x+y

            if next_num > num:
                break

            x = y
            y = next_num
            seq.append(next_num)

        return seq    



while True:
   d = input("Digite um número inteiro (ou 'e' para sair do programa): ") 
  
   if d =="e":
       print("------------------PROGRAMA FINALIZADO----------------")
       break
   
   num = int(d)
   
   seq = fibonacciSequenceUntilNum(num)

   if isinstance(seq, list) and num in seq:
        print(num ,"está na sequência")
   elif isinstance(seq, list) and num not in seq:
        print(num ,"não está na sequência")      

   print("--------------")
   print(seq)
   print("--------------")

