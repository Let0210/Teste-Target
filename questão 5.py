'''5) Escreva um programa que inverta os caracteres de um string.

      IMPORTANTE:
      a) Essa string pode ser informada através de qualquer entrada de sua preferência
      ou pode ser previamente definida no código;
      b) Evite usar funções prontas, como, por exemplo, reverse;'''

#-------------------------------------------------------

def stringReversed(str):
    index = len(str)-1
    str_rev=''

    while index>=0:
        str_rev += str[index]
        index -= 1

    return str_rev 

while True:
   str = input("\nDigite uma string (ou '0' para finalizar o programa): ")
  
   if str =="0":
       print("\n------------------PROGRAMA FINALIZADO----------------\n")
       break

   print(f"\nString ao contrário: {stringReversed(str)}")
    
