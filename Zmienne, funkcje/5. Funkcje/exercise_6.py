def calculate_net(gross, vat):
    if vat > 0 and vat <= 1:
        return gross * (1 - vat)
    else:
        print("Nieprawidlowa wartość podatku")


print(calculate_net(10, 0.23))
