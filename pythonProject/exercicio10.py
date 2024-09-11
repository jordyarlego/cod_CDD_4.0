soma=0
alunos = int(input("Quantos alunos tem na sua sala? "))
for x in range (1,alunos+1):
    notas=  float(input("Digite as notas dos alunos"))
    soma = soma+notas
media = soma / alunos
print(media)