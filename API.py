#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install requests')


# In[3]:


import requests


# In[4]:


url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)

print(req.status_code)


# In[5]:


#PEGA O MODELO JSON E TRANSOFRMA EM UM DICIONÁRIO

dados = req.json()

print(dados)


# In[6]:


valor_reais = float(input("Informe o valor em reais a ser convertido: \n"))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem US$ {(valor_reais / cotacao):.2f}')


# In[ ]:




