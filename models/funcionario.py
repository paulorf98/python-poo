from rich.table import Table
from rich.console import Console
from .pessoa import Pessoa

con = Console()

class Funcionario(Pessoa):

    cargos = ('docente', 'desenvolvedor', 'engenheiro de software')
    setores = ('suporte técnico', 'desenvolvimento de sistemas', 'gestão de dados')

    def __init__(self, nome, idade, hobby='Nenhum'):
        super().__init__(nome, idade)
        self.cargo: str | None = None
        self.setor: str | None = None
        self.hobby: str = hobby.strip()

    def definir_cargo(self, cargo):

        cargo = cargo.strip().lower()

        if self.cargo is not None:
            print(f'Você já trabalha no cargo {self.cargo}. Para alterá-lo, use "alterar_cargo".')
            return

        if cargo in self.cargos:
            self.cargo = cargo

        else:
            print('Cargo não disponível ou digitado incorretamente.')

    def alterar_cargo(self, new_cargo):

        new_cargo = new_cargo.strip().lower()

        if self.cargo is None:
            print('Você não trabalha em nenhum cargo. Para começar a trabalhar defina seu cargo em "definir_cargo".')
            return

        if new_cargo in self.cargos:
            self.cargo = new_cargo

        else:
            print('Cargo não disponível ou digitado incorretamente.')

    def definir_setor(self, setor):

        setor = setor.strip().lower()

        if self.setor is not None:
            print(f'Você trabalha no setor {self.setor}. Caso queira alterá-lo, use "alterar_setor".')
            return

        if setor in self.setores:
            self.setor = setor

        else:
            print('Setor não disponível ou digitado incorretamente.')

    def alterar_setor(self, new_setor):

        new_setor = new_setor.strip().lower()

        if self.setor is None:
            print('Você não trabalha em nenhum setor. Para trabalhar em um, use "definir_setor".')
            return

        if new_setor in self.setores:
            self.setor = new_setor

        else:
            print('Setor não disponível ou digitado incorretamente')

    def ver_dados_funcionario(self):

        if self.setor is None or self.cargo is None:
            print('Você ainda não trabalha aqui (cargo ou setor inválido(s))!')
            return

        tab3 = Table(title='Dados do Funcionário', title_style='bold magenta')

        tab3.add_column('Nome')
        tab3.add_column('Idade')
        tab3.add_column('Cargo')
        tab3.add_column('Setor')
        tab3.add_column('Hobby')

        tab3.add_row(
            self.nome.title(),
            str(self.idade),
            self.cargo.title(),
            self.setor.title(),
            self.hobby.title()
        )

        con.print(tab3)

    def definir_hobby(self, hobby):

        hobby = hobby.strip()

        if not hobby:
            print('Digite um hobby válido.')
            return

        self.hobby = hobby.lower()

    def ver_hobby(self):
        print(f'Hobby de {self.nome}: {self.hobby}')