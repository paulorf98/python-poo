from estudante import Estudante
from professor import Professor
from funcionario import Funcionario

def main():
    e = Estudante('Pedro', 20)

    e.ver_matricula() # Teste de erro
    e.fazer_matricula()
    e.ver_matricula()


    p = Professor('Kaique', 28)

    p.definir_especialidade('cyberseguranSSA')  # Teste de erro
    p.definir_titulo('banana')                  # Teste de erro
    p.definir_especialidade('cybersegurança')
    p.definir_titulo('graduação')
    p.dar_aula()
    p.ver_dados_professor()

    f = Funcionario('Amanda', 27)

    f.ver_dados_funcionario()                  # Teste de erro
    f.definir_cargo('')                        # Teste de erro
    f.definir_cargo('docente')
    f.definir_setor('gestão de dados')
    f.ver_dados_funcionario()
    f.alterar_cargo('')                        # Teste de erro
    f.alterar_setor('')                        # Teste de erro
    f.alterar_setor('suporte técnico')
    f.alterar_cargo('desenvolvedor')
    f.fazer_aniversario()
    f.definir_hobby('xadrez')
    f.ver_dados_funcionario()

if __name__ == '__main__':
    main()