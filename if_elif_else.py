valor = float(input())
saldo = valor

if valor > 0:
    #TODO: Imprimir a mensagem de sucesso, formatando o saldo atual (vide Exemplos).
   print(f"Deposito realizado com sucesso! Saldo atual: R${saldo}")
   
elif valor == 0:
   #TODO: Imprimir a mensagem de valor inválido.
   print(f"Encerrando o programa...")
else:
  #TODO: Imprimir a mensagem de encerrar o programa.
   print(f"Valor invalido! Digite um valor maior que zero.")
