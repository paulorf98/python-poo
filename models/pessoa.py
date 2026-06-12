from abc import ABC, abstractmethod # Abstract Base Class

class Pessoa(ABC):
    """Classe abstrata para todas as pessoas do sistema."""

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def ver_hobby(self):
        pass