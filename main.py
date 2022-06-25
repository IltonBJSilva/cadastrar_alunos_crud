import shutil, os
from time import sleep



#Função que vai criar o registro do aluno
def criarAluno(alunoid,nome, idade, epoca):
    diretorio = 'F:/Projetos Python/cadastrar_alunos_crud/Alunos.txt'
    arquivo = open(diretorio,'a')
    arquivo.writelines('Aluno ID:'+str(alunoid)+' Nome: '+nome+' Idade: '+idade+' Turma Escolar: '+epoca+'\n')
    arquivo.close()

def mostar_alunos(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    texto = arquivo.read()
    print(texto)
    arquivo.seek(0) #Voltar ao inicio do arquivo
    sleep(4)
    arquivo.close()

def atualizar_alunos(posicao):


    lista_aluno.remove(posicao)
    print('Removido com sucesso')
    print(lista_aluno)





if __name__ == '__main__':
    arquivo = 'F:/Projetos Python/cadastrar_alunos_crud/Alunos.txt'
    listarquivo = 'F:/Projetos Python/cadastrar_alunos_crud/lista_alunos.txt'

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
            contador = -1
            cont = 0
            while cont < qt_aluno:
                cont+=1
                contador+=1
                #Dicionario com as informações de alunos
                dic_alunos = ({'alunoid': [], 'aluno': [], 'idade': [], 'turma': []})
                aluno = str(input('Insira o nome dos alunos: '))
                idade = str(input('Insira a idade do aluno: '))
                epoca_escolar = str(input('Insira o ano escolar do aluno: '))
                #Inserindo no dicionario
                dic_alunos['alunoid'] = contador
                dic_alunos['aluno'] = aluno
                dic_alunos['idade'] = idade
                dic_alunos['turma'] = epoca_escolar
                #Chamandoa função para criar o registro
                criarAluno(contador,aluno, idade, epoca_escolar)
                #Adicionando o dicionario em uma lista de alunos
                lista_aluno.append(dic_alunos)
                print('Adicionando, um segundo...')

                #Salvar as informações da lista
                diretorio = 'F:/Projetos Python/cadastrar_alunos_crud/lista_alunos.txt'
                lista_file = open(diretorio, 'w')
                lista_file.write(str(lista_aluno))
                lista_file.close()

                sleep(1)
            print('Tudo adicionado com sucesso')
            print(lista_aluno)
        if opcao == 2: #Mostrar Arquivo
            if os.path.isfile(arquivo):
                #print(f'O caminho {arquivo} existe, estamos abrindo so um segundo...')
                sleep(1)
                print(lista_aluno)
                #print('Salvo... \n',mostar_alunos('Alunos.txt'))

            else:
                print('Não existe nenhum aluno cadastrado, deseja criar um registro?')
        if opcao == 3: #Atualizar informação
            if os.path.isfile(arquivo):
                indice = int(input('Qual deseja alterar:'.format(lista_aluno)))
                #Excluir o registro
                lista_aluno.pop(indice)
                #criar um novo dicionario
                dic_alunos = ({'alunoid': [], 'aluno': [], 'idade': [], 'turma': []})
                #Inserir os novos valores
                aluno = str(input('Insira o nome dos alunos: '))
                idade = str(input('Insira a idade do aluno: '))
                epoca_escolar = str(input('Insira o ano escolar do aluno: '))

                dic_alunos['alunoid'] = indice
                dic_alunos['aluno'] = aluno
                dic_alunos['idade'] = idade
                dic_alunos['turma'] = epoca_escolar
                criarAluno(contador,aluno, idade, epoca_escolar)

                #Adicionar a lista
                lista_aluno.insert(indice,dic_alunos)
                print(lista_aluno)


        if opcao == 4: #Excluir informação
            if os.path.isfile(arquivo):
                indice = int(input('Qual excluir qual:'.format(lista_aluno)))
                lista_aluno.pop(indice)

        else:
            print('Não existe nenhum aluno cadastrado, deseja criar um registro?')