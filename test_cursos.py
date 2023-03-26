import requests


class TestCursos:
    headers = {'Authorization': 'Token 625d558dc795babfa83e6ffd304fbd769a87f0f3'}
    url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

    def test_get_cursos(self):
        consulta_todos_os_cursos = requests.get(
            url=self.url_base_cursos, headers=self.headers)

        assert consulta_todos_os_cursos.status_code == 200

    def test_get_curso(self):
        consulta_curso = requests.get(
            url=f'{self.url_base_cursos}4/', headers=self.headers)

        assert consulta_curso.status_code == 200
        assert consulta_curso.json()['id'] == 4

    def test_post_curso(self):
        novo_curso = {
            'id': 7,
            'titulo': 'Gerencia Agil de Projetos com Scrum',
            'url': 'http://www.geekuniversity.com.br/scrum'
        }

        new_curso = requests.post(
            url=self.url_base_cursos, headers=self.headers, data=novo_curso)

        assert new_curso.status_code == 201

        atualizado = {
            'titulo': 'Novo Cruso - Gerencia Agil de Projetos com Scrum',
            'url': 'http://www.geekuniversity.com.br/newcursoscrum'
        }
        resposta = requests.put(
            url=f'{self.url_base_cursos}8/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200

    def test_put_titulo_curso(self):
        atualizado = {
            'titulo': 'Novo Cruso 2 - Gerencia Agil de Projetos com Scrum',
            'url': 'http://www.geekuniversity.com.br/newcursoscrum2'
        }
        resposta = requests.put(
            url=f'{self.url_base_cursos}8/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']

    def test_delete_curso_sem_autenticar(self):
        deletado = requests.delete(url=f'{self.url_base_cursos}8/')
        assert deletado.status_code == 401

    def test_delete_curso_autenticado(self):
        deletado = requests.delete(
            url=f'{self.url_base_cursos}8/', headers=self.headers)
        assert deletado.status_code == 204 and len(deletado.text) == 0
