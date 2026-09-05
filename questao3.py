# TÍTULO
print('Bem-vindos a Madeireira da Lenhadora Ana Paula Gomes Barbosa')

#VALORES DE CADA TIPO DE MADEIRA
PIN = 150.40
PER = 170.20
MOG = 190.90
IPE = 210.10
IMB = 220.70

# CRIAÇÃO DE PRIMEIRA FUNÇÃO PARA ESCOLHA DE TIPO DE TORA
def escolha_tipo():
    while True:
        print("Escolha o Tipo de Madeira desejado")
        print("PIN - Tora de Pinho")
        print("PER - Tora de Peroba")
        print("MOG - Tora de Mogno")
        print("IPE - Tora de Ipê")
        print("IMB - Tora de Imbuia")
        tipoMadeira = input(">> ")
        if tipoMadeira == "PIN":
            return PIN
        elif tipoMadeira == "PER":
            return PER
        elif tipoMadeira == "MOG":
            return MOG
        elif tipoMadeira == "IPE":
            return IPE
        elif tipoMadeira == "IMB":
            return IMB
        else:
            print("Escolha inválida, insira o modelo novamente.")


# CRIAÇÃO DE SEGUNDA FUNÇÃO PARA QTD DE TORAS
def qtd_toras():
    while True:
        print("Insira a quantidade de Toras")
        nToras = int(input(">> "))

        try:
            if nToras > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras. \n Por favor insira a quantidade novamente.")
                continue

            if nToras < 100:
                desconto = 0
            elif 100 <= nToras < 500:
                desconto = 0.04
            elif 500 <= nToras < 1000:
                desconto = 0.09
            elif 1000 <= nToras <= 2000:
                desconto = 0.16

            return nToras, desconto

        except ValueError:
             print("Escolha inválida. Insira uma quantidade válida.")

# CRIAÇÃO DE TERCEIRA FUNÇÃO PARA ESCOLHA DE TRANSPORTE
def transporte():
    while True:
        print("Escolha o tipo de Transporte")
        print("1 - Transporte Rodoviário - R$1000.00")
        print("2 - Transporte Ferroviário - R$2000.00")
        print("3 - Transporte Hidroviário - R$2500.00")
        transp = int(input(">>  "))
        if transp == 1:
            return 1000
        elif transp == 2:
            return 2000
        elif transp == 3:
            return 2500

# DEFINIÇÕES DE VARIÁVEIS E CÁLCULO FINAL
tipoMadeira = escolha_tipo()
nToras, desconto = qtd_toras()
total = ((tipoMadeira * nToras) * (1-desconto)) + transporte()

print(f"Total: R$ {total}")

