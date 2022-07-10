import os
import time

alunos_quantidade = input("Quantidade de alunos: ")

if(alunos_quantidade.isdigit()):
     alunos_quantidade = int(alunos_quantidade)

     i = 1
     alunos = []

     while i <= alunos_quantidade:
          nome = input("Nome do aluno: ")
          alunos.append(nome.capitalize())
          i += 1

     else:
         print("Aluno(s) adicionado(s) à lista.")


         for aluno in alunos:

           nota_1 = input(f'Primeira nota, aluno {aluno}: ')
           nota_2 = input(f'Segunda nota, aluno {aluno}: ')
           nota_3 = input(f'Terceira nota, aluno {aluno}: ')

           if(nota_1.isdigit() and nota_2.isdigit() and nota_3.isdigit()):
             nota_1 = float(nota_1)
             nota_2 = float(nota_2)
             nota_3 = float(nota_3)
             media = (nota_1 + nota_2 + nota_3) / 3
             # os.system("")
             print(f' Aluno: {aluno}, nota final: {media}')
             time.sleep(4)

           else:
            print("Informe apenas números.")

else:
     print("Informe apenas números!")


