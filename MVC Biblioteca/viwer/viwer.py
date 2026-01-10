from abc import ABC, abstractmethod

class View(ABC):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.model.adicionar_observer(self)
        self.ativa = False

    @abstractmethod
    def renderizar(self):
        pass

    @abstractmethod
    def update(self, msg):
        pass

    def ativar(self):
        self.ativa = True
        self.renderizar()

    def desativar(self):
        self.ativa = False

class ViewLista(View):

    def renderizar(self):
        dados = self.model.listar()
        print('-----LIVROS REGISTRADOS-----')
        for livro in dados:
            print (f"{livro.isbn} | {livro.titulo} | {livro.autor} | {'Disponivel' if not livro.emprestado else 'Indisponível'}")
            print(30*'-')

    def update(self, msg):
        if not self.ativa:
            return
        
        match msg:
            case 'emprestar' | 'devolver' | 'update' | 'create':
                self.renderizar()

class ViewDisponiveis(View):

    def renderizar(self):
        dados = self.model.listar()
        print('-----LIVROS DISPONIVEIS-----')
        for livro in dados:
            if not livro.emprestado:
                print (f"{livro.isbn} | {livro.titulo} | {livro.autor} | {'Disponivel' if not livro.emprestado else 'Indisponível'}")
                print(30*'-')

    def update(self, msg):
        if not self.ativa:
            return
        
        match msg:
            case 'emprestar' | 'devolver' | 'update' | 'create':
                self.renderizar()

class ViewDetalhes(View):

    def __init__(self, model):
        super().__init__(model)
        self.livro = None

    def set_livro(self, livro):
        self.livro = livro

    def renderizar(self):
        if not self.livro is None:
            livro = self.livro
            print (f"{livro.isbn} | {livro.titulo} | {livro.autor} | {'Disponivel' if not livro.emprestado else 'Indisponível'}")

    def update(self, msg):
        if not self.ativa: return
        match msg:
            case 'create' | 'update' | 'emprestar' | 'devolver':
                self.renderizar()