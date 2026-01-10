from model.ModelLivro import ModelLivro
from viwer.viwer import ViewLista, ViewDetalhes, ViewDisponiveis
from controller.controller import ControllerLivro

if __name__ == "__main__":
    # 1. Instancia o Cérebro
    model = ModelLivro()

    # 2. Instancia as Telas (conectando ao cérebro)
    v_lista = ViewLista(model)
    v_detalhes = ViewDetalhes(model)
    v_disponiveis = ViewDisponiveis(model)

    # 3. Instancia o Gerente (entregando as ferramentas)
    app = ControllerLivro(model, v_detalhes, v_disponiveis, v_lista)

    # 4. Ação!
    app.iniciar()