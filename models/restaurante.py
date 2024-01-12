from models.avalicao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio

class Restaurante:

    """
    Represents a restaurant with basic information and functionality.
    """

    restaurantes = []

    def __init__(self, nome, categoria):

        """
        Initializes a new instance of the Restaurante class.

        Parameters:
        - nome (str): The name of the restaurant.
        - categoria (str): The category of the restaurant.
        """

        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self):

        """
        Returns a string representation of the restaurant.

        Returns:
        str: A formatted string with the name and category of the restaurant.
        """

        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):

        """
        Prints a list of all restaurants with their information.
        """

        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}')

    @property
    def ativo(self):

        """
        Gets a string representing the state of the restaurant (active or inactive).

        Returns:
        str: '⌧' if active, '☐' if inactive.
        """

        return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):

        """
        Toggles the active/inactive state of the restaurant.
        """

        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):

        """
        Receives a customer's evaluation and adds it to the restaurant's evaluations.

        Parameters:
        - cliente (str): The name of the customer.
        - nota (float): The rating given by the customer (between 0.5 and 5.0).
        """

        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):

        """
        Calculates and returns the average rating of the restaurant.

        Returns:
        float or str: The average rating or '-' if no ratings are available.
        """

        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
      
    def adicionar_cardapio(self, item):
        """
        Adds an item to the restaurant's menu.

        Parameters:
        - item (ItemCardapio): The item to be added to the menu.

        Returns:
        - None
        """
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property  
    def exibir_cardapio(self):
        """
        Displays the restaurant's menu, including both dishes and drinks.

        Returns:
        - None
        """
        print(f'Cardapio do restaurate {self._nome}\n')
        
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição:{item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho:{item.tamanho}'
                print(mensagem_bebida)
