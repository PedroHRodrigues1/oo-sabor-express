from abc import ABC, abstractmethod

class ItemCardapio(ABC):

    """
    Abstract base class representing an item in the menu of a restaurant.

    Attributes:
    - nome (str): The name of the menu item.
    - preco (float): The price of the menu item.
    """

    def __init__(self, nome, preco):

        """
        Initializes a new instance of the ItemCardapio class.

        Parameters:
        - nome (str): The name of the menu item.
        - preco (float): The price of the menu item.
        """
        self._nome = nome
        self._preco = preco


    @abstractmethod
    def aplicar_desconto(self):

        """
        Abstract method to be implemented by subclasses.
        Applies a discount to the price of the menu item.

        Returns:
        - None
        """

        pass
