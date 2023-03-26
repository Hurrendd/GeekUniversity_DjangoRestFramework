import requests

# GET AVALIAÇÕES

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
print(avaliacoes.status_code)
# Acessando os dados da resposta
print(avaliacoes.json())
# Acessando a quatidade de item
print(avaliacoes.json()['count'])
# Acessando a proxima página
print(avaliacoes.json()['next'])

# Acessando os resultados e o primeiro elemento
print(avaliacoes.json()['results'])  # Aqui é uma lista
# Acessando o primeiro elemento da lista, Aqui ja é um dict novamente
print(avaliacoes.json()['results'][0])

print('Agora fazendo acesso a 1(uma) avaliação')
avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')
print(avaliacao.status_code)
print(avaliacao.json())

print('************************ Acessando os cursos ********************')
headers = {'Authorization': 'Token 625d558dc795babfa83e6ffd304fbd769a87f0f3'}
cursos = requests.get(
    url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.json())
