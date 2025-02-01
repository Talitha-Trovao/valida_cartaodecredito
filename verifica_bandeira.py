import logging

logging.basicConfig(level=logging.INFO)

def identificar_bandeira(numero_cartao):
    if numero_cartao.startswith('4'):
        return "Visa"
    elif numero_cartao.startswith(('51', '52', '53', '54', '55')):
        return "Mastercard"
    elif numero_cartao.startswith(('34', '37')):
        return "American Express"
    elif numero_cartao.startswith(('5', '6')):
        return "Elo"
    else:
        return "Bandeira desconhecida"

# Exemplo de uso
numero_cartao = input("Digite o número do cartão de crédito: ")
bandeira = identificar_bandeira(numero_cartao)
if bandeira == "Bandeira desconhecida":
    logging.info("False")
else:
    logging.info("True")
print(f"A bandeira do cartão é: {bandeira}")
