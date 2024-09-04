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
    
