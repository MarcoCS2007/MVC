# EXERCÍCIO 4: MVC para Sistema de Biblioteca
# =============================================
"""
Crie um sistema MVC para gerenciar livros de uma biblioteca.

Requisitos:
- Model Livro: gerencia livros (criar, listar, buscar, emprestar, devolver)
- View Livro: renderiza informações de livros de diferentes formas
- Controller Livro: coordena operações de biblioteca

Operações:
- Adicionar livro (título, autor, ISBN)
- Listar livros
- Buscar livro por título ou autor
- Emprestar livro (marca como emprestado)
- Devolver livro (marca como disponível)

Crie múltiplas views:
- ViewLista: lista todos os livros
- ViewDetalhes: mostra detalhes de um livro
- ViewDisponiveis: mostra apenas livros disponíveis
"""

# TODO: Implemente aqui
class ModelLivro:
    """Model para livros"""
    pass

class ViewLivro(ABC):
    """View abstrata para livros"""
    pass

class ControllerLivro:
    """Controller para livros"""
    pass