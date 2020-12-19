### Feito por Fellipe Domingues Fernandes para o teste Summer Job na Navi

import math
vector = [None]*10

for i in range(len(vector)):
    if (i % 2 == 0):
        vector[i] = pow(3,i) + 7*(math.factorial(i))
    else:
        vector[i] = pow(2,i) + 4*(math.log(i))

posLargest = vector.index(max(vector))
avgValue = round(sum(vector) / len(vector), 2)

print(f"O maior valor esta na posicao {posLargest}, e a media dos elementos deste vetor eh {avgValue}.")





