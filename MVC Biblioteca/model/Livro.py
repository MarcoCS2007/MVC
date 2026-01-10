class Livro:
    
    def __init__(self, isbn, titulo, autor):
        self._isbn = isbn
        self._titulo = titulo
        self._autor = autor
        self._emprestado = False

    @property
    def isbn(self):
        return self._isbn
    
    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor
    
    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def emprestado(self):
        return self._emprestado
    
    @emprestado.setter
    def emprestado(self, value: bool):
        self._emprestado = value

    def to_dict(self):
        return {
            'isbn': self._isbn,
            'titulo' : self._titulo,
            'autor' : self._autor,
            'emprestado': self._emprestado
        }