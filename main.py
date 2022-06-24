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
    arquivo = 'F:/Projetos Python/cadastrar_alunos_crud/Alunos.txt'
    lista_aluno = []
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
                dic_alunos = ({'alunoid': [], 'aluno': [], 'idade': [], 'turma': []})
                aluno = str(input('Insira o nome dos alunos: '))
                idade = str(input('Insira a idade do aluno: '))
                epoca_escolar = str(input('Insira o ano escolar do aluno: '))
                dic_alunos['alunoid'] = contador
                dic_alunos['aluno'] = aluno
                dic_alunos['idade'] = idade
                dic_alunos['turma'] = epoca_escolar
                criarAluno(aluno, idade, epoca_escolar)
                lista_aluno.append(dic_alunos)

                #lista_aluno.append(dic_alunos['alunoid'])
                # lista_aluno.append(dic_alunos['aluno'])
                # lista_aluno.append(dic_alunos['idade'])
                # lista_aluno.append(dic_alunos['turma'])


                print('Adicionando, um segundo...')
                sleep(1)
            print('Tudo adicionado com sucesso')
            print(lista_aluno)
        if opcao == 2: #Mostrar Arquivo
            if os.path.isfile(arquivo):
                print(f'O caminho {arquivo} existe, estamos abrindo so um segundo...')
                sleep(1)
                mostar_alunos('Alunos.txt')
            else:
                print('Não existe nenhum aluno cadastrado, deseja criar um registro?')
        if opcao == 3: #Atualizar informação
            if os.path.isfile(arquivo):
                indice = str(input(f'Qual deseja excluir?\n{lista_aluno}'))
                sleep(1)
                mostar_alunos('Alunos.txt')
            else:
                print('Não existe nenhum aluno cadastrado, deseja criar um registro?')



        else:
            print('Não existe essa opcao')
