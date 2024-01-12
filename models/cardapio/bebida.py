from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    """
    Represents a beverage in the menu of a restaurant.

    Attributes:
    - nome (str): The name of the beverage.
    - preco (float): The price of the beverage.
    - tamanho (str): The size of the beverage.
    """

    def __init__(self, nome, preco, tamanho):

        """
        Initializes a new instance of the Bebida class.

        Parameters:
        - nome (str): The name of the beverage.
        - preco (float): The price of the beverage.
        - tamanho (str): The size of the beverage.
        """

        super().__init__(nome, preco)
        self.tamanho = tamanho
        

    def __str__(self):

        """
        Returns a string representation of the Bebida object.

        Returns:
        - str: A formatted string containing the name, price, and size of the beverage.
        """
        return f'{self._nome} | {self._preco} | {self._tamanho}'


    def aplicar_desconto(self):
        """
        Applies a discount of 8% to the price of the beverage.

        Returns:
        - None
        """
        self._preco -= (self._preco * 0.08)