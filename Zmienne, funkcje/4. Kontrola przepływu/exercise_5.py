print("Równanie w postaci ax**2 + bx + c == 0")

a = int(input("Liczba a: "))
b = int(input("Liczba b: "))
c = int(input("Liczba c: "))

delta = b**2 - 4*a*c

if delta == 0:
    x12 = -b/2*a
    print(x12)
elif delta > 0:
    x1 = (-b - delta**(1/2))/2*a
    x2 = (-b + delta**(1/2))/2*a
    print(round(x1), round(x2))
else:
    print(f"{delta} < 0")
