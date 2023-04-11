def cria_conta(numero,saldo,titular,limite):
    conta = {"numero": numero, "saldo": saldo, "titular": titular, "limite":limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Seu extrato e {} reais".format(conta["saldo"]))
    