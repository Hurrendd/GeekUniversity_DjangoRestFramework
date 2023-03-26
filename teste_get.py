import requests

headers = {'Authorization': 'Token 625d558dc795babfa83e6ffd304fbd769a87f0f3'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

assert resultado.status_code == 200

assert resultado.json()['count'] == 4

assert resultado.json()['previous'] == None

assert resultado.json()[
    'results'][1]['titulo'] == 'Crie APIs REST com Python e Django REST Framework: Essencial'
