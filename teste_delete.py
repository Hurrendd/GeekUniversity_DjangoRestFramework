import requests

headers = {'Authorization': 'Token 625d558dc795babfa83e6ffd304fbd769a87f0f3'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(
    url=f'{url_base_cursos}6/', headers=headers)

assert resultado.status_code == 204

assert len(resultado.text) == 0
