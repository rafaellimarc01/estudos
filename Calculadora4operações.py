#Criação de um sistema de calculadora 

print("Bem-vindo a Calculadora")
print("Temos essas operações disponíveis na calculadora: soma, subtração, multiplicação e divisão")



while True:

    x = input("Qual operação você deseja?")
    
    if x == "soma":
     a = int(input("Qual o primeiro número?"))
     b = int(input("Qual o segundo número?"))
     c = a + b

     print("Sua resposta é {}".format(c))
     print("Obrigado por usar a calculadora!")
    

    elif x == "subtração":
     a = int(input("Qual o primeiro número?"))
     b = int(input("Qual o segundo número?"))
     c = a - b

     print("Sua resposta é {}".format(c))
     print("Obrigado por usar a calculadora!")

    elif x == "multiplicação":
     a = int(input("Qual o primeiro número?"))
     b = int(input("Qual o segundo número?"))
     c = a * b

     print("Sua resposta é {}".format(c))
     print("Obrigado por usar a calculadora!")

    elif x == "divisão":
     a = int(input("Qual o primeiro número?"))
     b = int(input("Qual o segundo número?"))
     c = a / b

     print("Sua resposta é {}".format(c))
     print("Obrigado por usar a calculadora!")

    else:
     print("Não é possivel efetuar uma operação com essa resposta")

   