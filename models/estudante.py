from .pessoa import Pessoa
from rich.table import Table
from rich.console import Console
from random import choice

con = Console()

class Estudante(Pessoa):

    cursos_and_turmas = {

        'ciência da computação': {
            'Turmas': ['2026a-Science', '2026b-Science']
        },

        'engenharia de software': {
            'Turmas': ['2026a-Engineering', '2026b-Engineering']
        },

        'cybersegurança': {
            'Turmas': ['2026a-Security', '2026b-Security']
        },

        'sistemas de informação': {
            'Turmas': ['2026a-Info System', '2026b-Info System']
        }
    }


    def __init__(self, nome, idade, hobby='Estudar'):
        super().__init__(nome, idade)
        self.curso: str = ''
        self.turma: str = ''
        self.hobby: str = hobby.strip()

    def fazer_matricula(self):

        while True:

            curso = input('Qual curso? ').strip().lower()

            if curso in self.cursos_and_turmas:
                self.curso = curso
                break

            print('Digite o nome do curso corretamente')

        self.turma = choice(
            self.cursos_and_turmas[self.curso]['Turmas']
        )


    def ver_matricula(self):

        if not self.curso or not self.turma:
            print('Você ainda não possui uma matrícula.')
            return

        tab = Table(title='Matrícula', title_style='bold magenta')

        tab.add_column('Nome')
        tab.add_column('Idade')
        tab.add_column('Curso')
        tab.add_column('Turma')
        tab.add_column('Hobby')

        tab.add_row(
            self.nome,
            str(self.idade),
            self.curso,
            self.turma,
            self.hobby.title()
        )

        con.print(tab)

    def ver_hobby(self):
        print(f"{self.nome} tem o costume de {self.hobby.lower()} para passar o tempo")