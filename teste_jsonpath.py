import jsonpath
import requests

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')
resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

print(resultados)

primeiro_elemento = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeiro_elemento)

nome_primeiro_elemento = jsonpath.jsonpath(
    avaliacoes.json(), 'results[0].nome')
print(nome_primeiro_elemento)

todos_nomes_avaliacao = jsonpath.jsonpath(
    avaliacoes.json(), 'results[*].nome')
print(todos_nomes_avaliacao)

notas = jsonpath.jsonpath(
    avaliacoes.json(), 'results[*].avaliacao')
print(notas)
