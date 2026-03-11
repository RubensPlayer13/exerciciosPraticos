'''Gerenciador de Tarefas - Um aplicativo simples para gerenciar
suas tarefas diárias. Este aplicativo permite adicionar,
listar, concluir e remover tarefas.'''
import json
import datetime


class GerenciadorDeTarefas:
    '''Classe para gerenciar tarefas, permitindo adicionar,
    listar, concluir e remover tarefas.
    As tarefas são armazenadas em um arquivo JSON.'''
    def __init__(self, arquivo='tarefas.json'):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        '''Carrega as tarefas do arquivo JSON.
        Se o arquivo não existir, retorna uma lista vazia.'''
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_tarefas(self):
        '''Salva as tarefas atuais no arquivo JSON.'''
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.tarefas, f, indent=4)

    def adicionar_tarefa(self, descricao, data_vencimento):
        '''Adiciona uma nova tarefa com a descrição e
          data de vencimento fornecidas.'''
        tarefa = {
            'descricao': descricao,
            'data_vencimento': data_vencimento,
            'data_criacao': datetime.datetime.now().isoformat(),
            'concluida': False
        }
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def listar_tarefas(self):
        '''Exibe todas as tarefas com seus detalhes.'''
        for idx, tarefa in enumerate(self.tarefas):
            status = 'Concluída' if tarefa['concluida'] else 'Pendente'
            print(
                f"{idx + 1}. {
                    tarefa['descricao']
                    } - Vencimento: {
                        tarefa['data_vencimento']
                        } - Status: {status}")

    def concluir_tarefa(self, indice):
        '''Marca a tarefa como concluída com base no índice fornecido.'''
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]['concluida'] = True
            self.salvar_tarefas()
        else:
            print("Índice inválido.")

    def remover_tarefa(self, indice):
        '''Remove a tarefa com base no índice fornecido.'''
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self.salvar_tarefas()
        else:
            print("Índice inválido.")


if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Concluir Tarefa")
        print("4. Remover Tarefa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao_ = input("Descrição da tarefa: ")
            data_vencimento_ = input("Data de vencimento (YYYY-MM-DD): ")
            gerenciador.adicionar_tarefa(descricao_, data_vencimento_)
        elif escolha == '2':
            gerenciador.listar_tarefas()
        elif escolha == '3':
            indice_ = int(input("Índice da tarefa a concluir: ")) - 1
            gerenciador.concluir_tarefa(indice_)
        elif escolha == '4':
            indice_ = int(input("Índice da tarefa a remover: ")) - 1
            gerenciador.remover_tarefa(indice_)
        elif escolha == '5':
            break
        else:
            print("Opção inválida. Tente novamente.")
