from model.Livro import Livro

class ModelLivro:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._inicializado = False
        return cls._instance         

    def __init__(self):
        if not self._inicializado:
            self._observadores = []
            self._dados = []
            self._inicializado = True

    def _notificar(self, msg):
        for obs in self._observadores:
            obs.update(msg)

    def adicionar_observer(self, observer):
        if observer not in self._observadores:
            self._observadores.append(observer)

    def criar_atualizar(self, isbn, titulo, autor):
        livro = self.obter_isbn(isbn)
        if livro:
            livro.titulo = titulo
            livro.autor = autor
            self._notificar('update')
            return None
        livro = Livro(isbn, titulo, autor)
        self._dados.append(livro)
        self._notificar('create')
        return None  

    def listar(self) -> list:
        return self._dados[:]
    
    def obter_isbn(self, isbn):
        for livro in self._dados:
            if livro.isbn == isbn:
                return livro
        return None

    def buscar(self, busca) -> Livro:
        livros = []
        for livro in self._dados:
            if busca in livro.isbn or busca in livro.titulo or busca in livro.autor:
                livros.append(livro)
        return livros

    def emprestar(self, livro: Livro):
        if livro.emprestado:
            raise ValueError 
        livro.emprestado = True
        self._notificar('emprestar')

    def devolver(self, livro:Livro):
        if not livro.emprestado:
            raise ValueError 
        livro.emprestado = False
        self._notificar('devolver')