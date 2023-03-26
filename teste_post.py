import requests

headers = {'Authorization': 'Token 625d558dc795babfa83e6ffd304fbd769a87f0f3'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    'titulo': 'Gerencia Agil de Projetos com Scrum',
    'url': 'http://www.geekuniversity.com.br/scrum'
}

resultado = requests.post(
    url=url_base_cursos, headers=headers, data=novo_curso)

# Testando o codigo de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']
