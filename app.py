from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida

churrascaria = Restaurante('Churras', 'Churrascaria')
bebida_coca = Bebida('Coca Cola', 10.00, '2L')
bebida_coca.aplicar_desconto()
prato_feijoada = Prato('Feijoada', 50.00, 'A melhor feijoada da Cidade')
prato_feijoada.aplicar_desconto()

churrascaria.adicionar_cardapio(bebida_coca)
churrascaria.adicionar_cardapio(prato_feijoada)


def main():
    churrascaria.exibir_cardapio


if __name__ == '__main__':
    main()
