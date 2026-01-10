from models.ModelProduto import ModelProduto
from models.Produtos import Produto
import json
from abc import ABC, abstractmethod

class ViewAPI(ABC):
    
    @abstractmethod
    def renderizar(self):
        pass