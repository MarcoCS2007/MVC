from model.ModelLivro import ModelLivro
# Cuidado com o typo na pasta: 'viwer' -> ideal seria 'views' ou 'viewer'
from viwer.viwer import ViewDetalhes, ViewDisponiveis, ViewLista

class ControllerLivro:

    def __init__(self, model: ModelLivro, viewDetalhes: ViewDetalhes, viewDisponiveis: ViewDisponiveis, viewLista: ViewLista):
        self.model = model
        self.viewDetalhes = viewDetalhes
        self.viewDisponiveis = viewDisponiveis
        self.viewLista = viewLista

    def iniciar(self):
        """O Loop Principal que mantém o programa rodando"""
        while True:
            print("\n--- MENU ---")
            print("1. Listar Livros")
            print("2. Listar Disponíveis")
            print("3. Buscar/Detalhes")
            print("4. Emprestar")
            print("5. Devolver")
            print("6. Cadastrar")
            print("0. Sair")
            
            opcao = input("Opção: ")

            match opcao:
                case '1': self.fluxo_listar()
                case '2': self.fluxo_disponiveis()
                case '3': self.fluxo_buscar_detalhes()
                case '4': self.fluxo_emprestar() # <--- O que faltava
                case '5': self.fluxo_devolver()  # <--- O que faltava
                case '6': self.fluxo_criar()
                case '0': break
                case _: print("Opção inválida")

    # --- FLUXOS DE AÇÃO ---

    def fluxo_listar(self):
        # Ativa a view, espera o usuário ler, e desativa
        self.viewLista.ativar()
        input("Enter para voltar...")
        self.viewLista.desativar()

    def fluxo_disponiveis(self):
        self.viewDisponiveis.ativar()
        input("Enter para voltar...")
        self.viewDisponiveis.desativar()

    def fluxo_criar(self):
        # O Controller coleta os dados (input)
        isbn = input("ISBN: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        
        # E manda o Model trabalhar
        try:
            self.model.criar_atualizar(isbn, titulo, autor)
            print("Livro salvo com sucesso!")
        except ValueError as e:
            print(f"Erro ao salvar: {e}")

    def fluxo_buscar_detalhes(self):
        busca = input("Digite o ISBN, Título ou Autor: ")
        resultados = self.model.buscar(busca)

        if not resultados:
            print("Nenhum livro encontrado.")
            return

        # Se achou apenas um livro, já mostra os detalhes dele
        if len(resultados) == 1:
            livro = resultados[0]
            self.viewDetalhes.set_livro(livro) # Prepara
            self.viewDetalhes.ativar()         # Mostra
            input("Enter para sair...")
            self.viewDetalhes.desativar()      # Limpa
        else:
            # Se achou vários, lista eles (reuso de lógica!)
            print(f"Foram encontrados {len(resultados)} livros. Refine sua busca.")
            for l in resultados:
                print(f"- {l.titulo} ({l.isbn})")

    # --- OS MÉTODOS QUE FALTAVAM ---

    def fluxo_emprestar(self):
        # 1. Ajuda o usuário mostrando o que tem disponível
        self.viewDisponiveis.ativar()
        
        isbn = input("\nDigite o ISBN para emprestar: ")
        livro = self.model.obter_isbn(isbn)

        if livro:
            try:
                self.model.emprestar(livro)
                print("Sucesso! Bom proveito.")
            except ValueError:
                print("ERRO: Este livro já está emprestado!")
        else:
            print("Livro não encontrado.")
        
        self.viewDisponiveis.desativar()

    def fluxo_devolver(self):
        isbn = input("Digite o ISBN para devolver: ")
        livro = self.model.obter_isbn(isbn)

        if livro:
            try:
                self.model.devolver(livro)
                print("Livro devolvido. Obrigado!")
            except ValueError:
                print("ERRO: Este livro não consta como emprestado.")
        else:
            print("Livro não encontrado.")