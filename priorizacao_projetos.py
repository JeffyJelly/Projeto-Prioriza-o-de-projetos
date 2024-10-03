#python program
# from types import DynamicClassAttribute
from rich import print #biblioteca para decoração.
from rich.table import Table #biblioteca para tabela.
import os #biblioteca para limpar o console ao resetar o loop e para os.path.isfile() para verificar se existe uma pasta específica salva.
import pickle

dicionario_atividades_prioridades={}
atividade=" "
while True:
  #Menu de opções, 6 opções de funções do programa e uma opção de sair.
  os.system("clear")
  print('''
  0- Sair
  1- Adicionar Atividade e prioridade
  2- Remover Atividade
  3- Mudar Prioridade
  4- Mostrar tudo
  5- Mostrar uma Atividade
  6- Salvar/Recuperar dados

  ''')
  opcao=int(input("Selecione uma opção:\n"))
  
  if opcao == 0:
    print("Parando programa...")
    break

  #Adicionar atividade e valor de prioridade relacionada.
  #O usuário insere o nome da atividade e o valor de prioridade dessa atividade.
  #Também mostrando a atividade e o valor de prioridade relacionada.
  elif opcao == 1:
    atividade=input("Informe o nome da atividade que deseja adicionar:\n")
    prioridade=input(f"Informe o valor de prioridade para {atividade}. (Número):\n")
    # prioridade_int=int(prioridade, base)#try except é usado para tentar converter um número em de sting para int
    try:
      int(prioridade)
      dicionario_atividades_prioridades[atividade]=prioridade
      print(f"A atividade '{atividade}' com prioridade '{prioridade}' foi cadastrada!")
    
    except:
      print(f"{prioridade} não é um número inteiro!")

  
  #Segunda opção: Remover atividade: Checando se a atividade está cadastrada, remove a atividade escolhida.
  #Funcionando
  elif opcao == 2:
    atividade=input("Informe a atividade que deseja remover:\n")
    if atividade in dicionario_atividades_prioridades:
      del dicionario_atividades_prioridades[atividade]
      print(f"{atividade} deletada!")
    else:
      print(f"{atividade} não existe!")


  #Mudar prioridade de alguma Atividade:
  elif opcao == 3:
    atividade=input("Informe a atividade que deseja mudar o valor de prioridade:\n")
    if atividade in dicionario_atividades_prioridades:
      prioridade=float(input(f"Informe o valor de prioridade para {atividade} (número):\n"))
      dicionario_atividades_prioridades[atividade]=prioridade
      print(f"{atividade} agora tem prioridade igual a {prioridade:.2f}!")
    else:
      print(f"{atividade} não está cadastrado!")

  #Mostrar lista de atividades e os valores relacionados em uma tabela por meio da biblioteca "Table".
  elif opcao == 4:
    if dicionario_atividades_prioridades!= {}:
      #Verificar forma de prioridade para mostrar tabela:
      
      print("""
      1- Decrescente
      2- Crescente
      """)
      prioridade=int(input("Selecione a opção com a forma de prioridade desejada:\n"))
      
      table=Table(title=f"[purple]Priorização de Atividades", expand=True, style="purple")
      table.add_column("ATIVIDADES", justify="center", style="red")
      table.add_column("PRIORIDADE", justify="center", style="blue")
      dicionario_atividades_prioridades_crescente=sorted(dicionario_atividades_prioridades)
      if prioridade == 1: #Mostrar tabela em ordem crescente
        for atividade in dicionario_atividades_prioridades_crescente:
          table.add_row(f"[red]{atividade}[/red]",f"{dicionario_atividades_prioridades[atividade]}")
        print(table)
          
      elif prioridade == 2: #Mostrar tabela em ordem decrescende
        for atividade in reversed(dicionario_atividades_prioridades_crescente):
          table.add_row(f"[red]{atividade}[/red]",f"{dicionario_atividades_prioridades[atividade]}")
        print(table)
    else:
      print("Não há atividades cadastradas!")
  
  elif opcao == 5:
    atividade=input("Digite o nome da Atividade:\n")
    if atividade in dicionario_atividades_prioridades:
      print(f"[red]{atividade}[/red] - {dicionario_atividades_prioridades[atividade]}")
    else:
      print("Atividade não cadastrada!")    

  #Opção 6 para salvar/recuperar dados cadastrados em uma pasta:
  elif opcao == 6:
    print("""
    1-Salvar Atividades
    2-Recuperar Atividades
    """)
    salvar_recuperar=int(input("Selecione uma opção acima:\n"))
    
    if salvar_recuperar == 1:
      if dicionario_atividades_prioridades!={}:#Teste para verificar se existem atividades no dicionário para salvar.
        
        nome_arquivo=input("Informe o nome do arquivo:\n")
        if os.path.isfile(nome_arquivo) == True: #Teste para verificar se o arquivo digitado existe.
          
          arquivo=open(nome_arquivo, 'wb')
          pickle.dump(dicionario_atividades_prioridades, arquivo)
          arquivo.close()
          print("Atividades salvas!")
          
        else:
          print(f"Arquivo \"{nome_arquivo}\" não existe")
      else:
        print("Não existe atividades a serem salvas!")
        
    elif salvar_recuperar == 2:
      nome_arquivo=input("Informe o nome do arquivo:\n")
      if os.path.isfile(nome_arquivo) == True:
        
        arquivo=open(nome_arquivo, 'rb')
        #Teste para verificar o tamanho do arquivo usando 'os.path.getsize()', se for 0 o arquivo está vazio.
        if os.path.getsize(nome_arquivo) != 0:
          dicionario_atividades_prioridades=pickle.load(arquivo)
          arquivo.close()
          print("Atividades recuperadas!")
        else:
          print(f"Arquivo \"{nome_arquivo}\" está vazio!")
      else:
        print(f"Arquivo \"{nome_arquivo}\" não existe!")
  else:
    print("Opção inválida!")
    
  input("Pressione Enter...")
