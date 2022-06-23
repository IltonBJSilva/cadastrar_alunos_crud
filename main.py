import shutil
from time import sleep


#Função que vai criar o registro do aluno
def criarAluno(nome, idade, epoca):
    diretorio = 'F:/Projetos Python/cadastrar_alunos_crud/Alunos.txt'
    arquivo = open(diretorio,'a')
    arquivo.writelines('\nNome: '+nome+'\nIdade: '+idade+'\nTurma Escolar: '+epoca+'\n')
    arquivo.close()





if __name__ == '__main__':
    opcao = int(input('Oque deseja fazer?\n01 - Cadastrar Aluno\n02 - Mostrar Alunos cadastrado\n03 - Atualizar Registro'
                      '04 - Excluir registro\nEscolha de acordo com o numero sem o zero: '))
    if opcao == 1:
        qt_aluno = int(input('Insira a quantidade de alunos que vão ser cadastrada:'))
        contador = 0
        while contador < qt_aluno:
            contador+=1
            aluno = str(input('Insira o nome dos alunos: '))
            idade = str(input('Insira a idade do aluno: '))
            epoca_escolar = str(input('Insira o ano escolar do aluno: '))
            criarAluno(aluno,idade,epoca_escolar)
            print('Adicionando, um segundo...')
            sleep(1)
        print('Tudo adicionado com sucesso')

