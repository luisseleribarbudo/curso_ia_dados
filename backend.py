### Qual linguagem?
### Quais ferramentas (framework)?
### Como e onde hospedar?

#### Metodos:
#    - Get - visualizando
#    - post - criando/postando/inserindo

#Desenvolvimento backend -----> API ________ CLIENTE (USUARIO) <> GARÇOM (API) <> COZINHA (MACHINE LEARNING) 

#viacep.com.br/us/13477540/json

import requests 

cep = input('Insira o seu CEP: ')

url = f'https://viacep.com.br/ws/{cep}/json/'

dados = requests.get(url)
resposta = dados.json()

print(resposta['logradouro'])