#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[6]:


with open('C:/Users/Augusto/Documents/ALEXANDRE/Lets Code/Material/Modulo 3 - Aplicações/arquivos/brasil_covid.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)


# In[8]:


with open('C:/Users/Augusto/Documents/ALEXANDRE/Lets Code/Material/Modulo 3 - Aplicações/arquivos/brasil_covid.csv', 'r') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)


# In[11]:


with open('users.csv', 'w', newline='') as arquivo_users:
        escritor = csv.writer(arquivo_users)
        escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
        escritor.writerow(['Alexandre', 'Barbosa', 'ale@email.com', 'Masculino'])
    


# In[16]:


header = ['nome', 'sobrenome']
dados = []
opt = input("O que deseja fazer?\n1- Cadastrar\n0 - Sair\n")
while opt != '0':
    nome = input("Qual é o seu nome?")
    sobrenome = input("Qual é o seu sobrenome?")
    dados.append([nome, sobrenome])
    opt = input("O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n")
    
print(dados)

with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)
    
with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)


# In[ ]:




