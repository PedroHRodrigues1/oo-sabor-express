from models.restaurante import Restaurante


churrascaria = Restaurante('Churras', 'Churrascaria')
churrascaria.receber_avaliacao('Pedro', 10)
churrascaria.alternar_estado()

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()