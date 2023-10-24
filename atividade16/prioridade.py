# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não.

pergunta = int(input("se você é gestante, idoso, cadeirante ou tem alguma disfunção cognitivas digite 1, se não se enquadra em nenhuma das alternativas anteriores digite 0: "))
if pergunta == 1:
    print("você pode ter acesso a fila de prioridade")
else:
    print("voê não pode ter acesso a fila de prioridade")