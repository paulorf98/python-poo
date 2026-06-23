from .pessoa import Pessoa
from rich.table import Table
from rich.console import Console


con = Console()

class Professor(Pessoa):

    especialidades = (
        'ciência da computação',
        'engenharia de software',
        'cybersegurança',
        'sistemas de informação'
    )

    titulacoes = (
        'graduação',
        'mestrado',
        'doutorado'
    )

    def __init__(self, nome, idade, hobby='Planejar sua próxima aula'):
        super().__init__(nome, idade)
        self.especialidade: str | None = None
        self.titulacao: str | None = None
        self.anos_de_experiencia: int = 0
        self.hobby: str = hobby.strip()

    def definir_especialidade(self, especialidade) -> None:

        especialidade = especialidade.strip().lower()

        if especialidade not in self.especialidades:
            print('Especialidade inválida')
            return

        self.especialidade = especialidade

    def definir_titulo(self, titulacao) -> None:

        titulacao = titulacao.strip().lower()

        if titulacao not in self.titulacoes:
            print('Título inválido!')
            return

        self.titulacao = titulacao

    def dar_aula(self):

        if self.especialidade is None:
            print('Não tem como dar aula sem uma especialidade antes.')
            return

        self.anos_de_experiencia += 1


    def ver_dados_professor(self):
        if self.especialidade is None or self.titulacao is None:
            print(f'Não foi possível visualizar os dados de {self.nome}.')
            return

        tab2 = Table(title='Dados do Professor', title_style='bold magenta')

        tab2.add_column('Nome')
        tab2.add_column('Idade')
        tab2.add_column('Especialidade')
        tab2.add_column('Título')
        tab2.add_column('Anos de Experiência')
        tab2.add_column('Hobby')

        tab2.add_row(
            self.nome,
            str(self.idade),
            self.especialidade,
            self.titulacao,
            str(self.anos_de_experiencia),
            self.hobby.title()
        )

        con.print(tab2)

    def ver_hobby(self):
        print(f'{self.nome} gosta de {self.hobby.lower()} para passar o tempo')