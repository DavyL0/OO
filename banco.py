import test

def banco(): 
    numero = int(input("Qual e o numero da sua conta? "))
    saldo =  int(input("Qual e o saldo da sua conta? "))
    titular = input("Quem e o titular da sua conta? ")
    limite = int(input("Qual e o seu limite"))
    
    print("****************************")
    print("****************************")
    print("*******Banco Davy!**********")
    print("****************************")
    print("****************************")

    print("vamos criar uma conta!")
    numero
    saldo
    titular
    limite

    print("O que deseja ver?")
    print("Depositar?(1)")
    print("Sacar?(2)")
    print("Ver extrato?(3)")
    escolha = int(input("Digite o nnumero "))

    if(escolha == 1):
        test.deposita
    elif(escolha == 2):
        test.saca
    elif(escolha == 3):
        test.extrato

    
