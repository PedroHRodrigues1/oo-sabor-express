

class Avaliacao:
    """
    Represents a customer's evaluation of a restaurant.
    """

    def __init__(self, cliente, nota):

        """
        Initializes a new instance of the Avaliacao class.

        Parameters:
        - cliente (str): The name of the customer providing the evaluation.
        - nota (float): The rating given by the customer (between 0.5 and 5.0).
        """

        self._cliente = cliente
        self._nota = nota
