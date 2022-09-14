#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as r


# In[2]:


url = 'https://api.covid19api.com/dayone/country/brazil'
response = r.get(url)


# In[3]:


response.status_code


# In[4]:


raw_data = response.json()


# In[5]:


raw_data[0]


# In[6]:


final_data = []

#PARA CADA UMA DAS NOSSA OBS ENCONTRADAS NOS NOSSOS DADOS BRUTOS
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])


# In[7]:


final_data.insert(0, ['Confirmados', 'Obitos', 'Recuperados', 'Ativos', 'Data' ])
final_data


# In[8]:


CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4


# In[9]:


for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]


# In[10]:


final_data


# In[11]:


import datetime as dt


# In[12]:


print(dt.time(12, 6, 21, 7), 'Hora:Minuto:Segundo:Microsegundo')
print('-----')
print(dt.date(2022, 9, 14), 'Ano-mês-dia')
print('-----')
print(dt.datetime(2022, 9, 14, 11, 43, 40, 9), 'Ano-mês-dia Hora:Minuto:Segundo:Microsegundo')


# In[13]:


natal = dt.date(2022, 12, 25)
reveillon = dt.date(2023, 1, 1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)


# In[14]:


import csv


# In[15]:


with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)


# In[16]:


for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')


# In[17]:


final_data


# In[18]:


def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return[
            {
                'label': labels[0],
                'data': y
            }
        ]


# In[19]:


def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }


# In[20]:


def create_chart(x, y, labels, kind='bar', title=''):
    
    datasets = get_datasets(y, labels)
    options = set_title(title)
    
    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    
    return chart


# In[30]:


#RETORNA A IMAGEM

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    response = r.get(f'{url_base}?c={str(chart)}')
    return response.content


# In[31]:


#SALVAR A IMAGEM

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


# In[32]:


from PIL import Image
from IPython.display import display


# In[33]:


def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


# In[34]:


y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])
    
y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))
    
chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')


# In[41]:


from urllib.parse import quote


# In[44]:


def get_api_qrcode(link):
    text = quote(link)
    url_base = 'https://quickchart.io/qr'
    response = r.get(f'{url_base}?text={text}')
    return response.content


# In[47]:


url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')


# In[ ]:




