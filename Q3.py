### DESAFIO 3 ###
### Como não foi requisitado um critério de desempate caso as maiores notas sejam iguais, o critério padrão será a ordem no nome no dicionário

### E também como o exercício ficou sucinto na explicação, decidi que o usuário é quem define os nomes e notas via função input, visto que
### não foi nos dado uma tabela de informações para alimentar o programa, além disso, não foi especificado o intervalo em que as notas devem variar
### (0 a 10, 0 a 100, etc). Com isso, as notas podem assumir qualquer valor real.

### Feito por Fellipe Domingues Fernandes para o teste Summer Job na Navi

numeroTotalAlunos = 5
boletim = {}

for x in range (numeroTotalAlunos):
    aluno = input(f"Digite o nome do aluno(a) numero {x+1}: ")
    boletim.update({aluno: None})

for i in boletim:
    boletim[i] = float(input(f"Digite a nota do aluno(a) {i}: "))

melhorAluno = max(boletim, key=boletim.get)
notas = tuple(boletim.values())
melhorNota = (max(notas))

print("QUESTAO 3")
print(f"O aluno(a) com maior nota é {melhorAluno}, com nota {melhorNota}.\n")