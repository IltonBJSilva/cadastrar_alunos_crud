import shutil, os
from time import sleep


#Função que vai criar o registro do aluno
def criarAluno(nome, idade, epoca):
    diretorio = 'F:/Projetos Python/cadastrar_alunos_crud/Alunos.txt'
    arquivo = open(diretorio,'a')
    arquivo.writelines('\nNome: '+nome+'\nIdade: '+idade+'\nTurma Escolar: '+epoca+'\n')
    arquivo.close()

def mostar_alunos(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)
    arquivo.seek(0) #Voltar ao inicio do arquivo
    sleep(4)
    arquivo.close()


if __name__ == '__main__':
    arquivo = 'F:/Projetos Python/cadastrar_alunos_crud/Alunos.txt'    lista_alunos = {'aluno':'','idade':'','turma':''}
    while True:
        opcao = int(input('Oque deseja fazer?\n00 - Fechar \n01 - Cadastrar Aluno\n02 - Mostrar Alunos cadastrado\n03 - Atualizar Registro'
                  '\n04 - Excluir registro\nEscolha de acordo com o numero sem o zero: '))
        if opcao == 0:
            print('Fechando...')
            sleep(1)
            break
        if opcao == 1: #Criar Arquivo
            qt_aluno = int(input('Insira a quantidade de alunos que vão ser cadastrada:'))
            contador = 0
            while contador < qt_aluno:
                contador+=1
                aluno = str(input('Insira o nome dos alunos: '))
                idade = str(input('Insira a idade do aluno: '))
                epoca_escolar = str(input('Insira o ano escolar do aluno: '))
                lista_alunos['aluno'] = aluno
                lista_alunos['idade'] = idade
                lista_alunos['turma'] = epoca_escolar
                criarAluno(aluno, idade, epoca_escolar)

                print('Adicionando, um segundo...')
                sleep(1)
            print('Tudo adicionado com sucesso')
            print(lista_alunos)

        if opcao == 2: #Mostrar Arquivo
            if os.path.isfile(arquivo):
                print(f'O caminho {arquivo} existe, estamos abrindo so um segundo...')
                sleep(1)
                mostar_alunos('Alunos.txt')
            else:
                print('Não existe nenhum aluno cadastrado, deseja criar um registro?')

        else:
            print('Não existe essa opcao')
