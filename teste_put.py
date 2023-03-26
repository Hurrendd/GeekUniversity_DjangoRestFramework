import requests

headers = {'Authorization': 'Token 625d558dc795babfa83e6ffd304fbd769a87f0f3'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    'titulo': 'Novo curso de Scrum 3',
    'url': 'http://www.geekuniversity.com.br/ncs3',
}
# Buscando curso com ID 6
# curso = requests.get(url=f'{url_base_cursos}6/', headers=headers)
# print(curso.json()['id'])

resultado = requests.put(
    url=f'{url_base_cursos}6/', headers=headers, data=curso_atualizado)

# Testando o codigo de status HTTP
assert resultado.status_code == 200

# Testando se o titulo foi atualizado
assert resultado.json()['titulo'] == curso_atualizado['titulo']
