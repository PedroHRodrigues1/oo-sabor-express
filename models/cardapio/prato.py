from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):

    """
    Represents a dish in the menu of a restaurant.

    Attributes:
    - nome (str): The name of the dish.
    - preco (float): The price of the dish.
    - descricao (str): The description of the dish.
    """

    def __init__(self, nome, preco, descricao):
        """
        Initializes a new instance of the Prato class.

        Parameters:
        - nome (str): The name of the dish.
        - preco (float): The price of the dish.
        - descricao (str): The description of the dish.
        """

        super().__init__(nome, preco)
        self.descricao = descricao
        
    def __str__(self):

        """
        Returns a string representation of the Prato object.

        Returns:
        - str: A formatted string containing the name, price, and description of the dish.
        """
        return f'{self._nome} | {self._preco} | {self._descricao}'


    def aplicar_desconto(self):

        """
        Applies a discount of 5% to the price of the dish.

        Returns:
        - None
        """
        self._preco -= (self._preco * 0.05)