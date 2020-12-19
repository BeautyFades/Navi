### Feito por Fellipe Domingues Fernandes para o teste Summer Job na Navi

def findNumbers(start=1,upTo=5000000):
    found = []
    for x in range (start, upTo+1):
        if (x % 2 == 0) and (x % 49 == 0) and (x % 37 == 0):
            found.append(x)
    print(f"Existem {len(found)} numeros entre {start} e {upTo} que sao pares, multiplos de 49 e de 37 ao mesmo tempo.")

findNumbers()