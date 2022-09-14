#!/usr/bin/env python
# coding: utf-8

# In[9]:


arquivo = open('C:/Users/Augusto/Documents/ALEXANDRE/Lets Code/Python Basics/3 - Aplicações/dom_casmurro.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()


# In[11]:


arquivo = open('C:/Users/Augusto/Documents/ALEXANDRE/Lets Code/Python Basics/3 - Aplicações/dom_casmurro.txt', 'r')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()


# In[12]:


arquivo = open('C:/Users/Augusto/Documents/ALEXANDRE/Lets Code/Python Basics/3 - Aplicações/dom_casmurro.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()


# In[13]:


with open('C:/Users/Augusto/Documents/ALEXANDRE/Lets Code/Python Basics/3 - Aplicações/dom_casmurro.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)


# In[14]:


arquivo.read()


# In[15]:


with open('arquivo_test.txt', 'w') as arquivo:
    arquivo.write('Esssa é uma linha que escrevi usando Python\n')
    arquivo.write('Esssa é a segunda linha que escrevi usando Python\n')


# In[16]:


with open('arquivo_test.txt', 'r') as arquivo:
    print(arquivo.read(), end='')


# In[17]:


with open('arquivo_test.txt', 'a') as arquivo:
    arquivo.write('Essa é a terceira linha que escrevi usando Python\n')


# In[18]:


with open('arquivo_test.txt', 'r') as arquivo:
    print(arquivo.read(), end='')


# In[ ]:




