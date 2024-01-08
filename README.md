# Avaliação de Restaurantes

Este é um aplicativo simples em Python que simula a gestão de avaliações para restaurantes. O aplicativo consiste em duas classes principais: Restaurante e Avaliacao.

Classe Restaurante
A classe Restaurante representa um restaurante com informações básicas e funcionalidades associadas.

Métodos
__init__(self, nome, categoria)

Inicializa uma nova instância da classe Restaurante.
Parâmetros:
nome (str): O nome do restaurante.
categoria (str): A categoria do restaurante.
__str__(self)

Retorna uma representação de string formatada do restaurante.
listar_restaurantes(cls)

Imprime uma lista de todos os restaurantes com suas informações.
ativo(self)

Obtém uma string representando o estado do restaurante (ativo ou inativo).
alternar_estado(self)

Alterna o estado ativo/inativo do restaurante.
receber_avaliacao(self, cliente, nota)

Recebe a avaliação de um cliente e a adiciona às avaliações do restaurante.
Parâmetros:
cliente (str): O nome do cliente.
nota (float): A avaliação dada pelo cliente (entre 0,5 e 5,0).
media_avaliacoes(self)

Calcula e retorna a média das avaliações do restaurante.
Propriedades
ativo

Obtém uma representação gráfica do estado do restaurante.
media_avaliacoes

Calcula e retorna a média das avaliações do restaurante.
Classe Avaliacao
A classe Avaliacao representa a avaliação de um cliente para um restaurante.

Método
__init__(self, cliente, nota)
Inicializa uma nova instância da classe Avaliacao.
Parâmetros:
cliente (str): O nome do cliente que fornece a avaliação.
nota (float): A avaliação dada pelo cliente (entre 0,5 e 5,0).
O código principal (app.py) demonstra a criação de uma instância de Restaurante chamada 'Churras', a recepção de uma avaliação e a alternância do estado do restaurante entre ativo e inativo. A função main lista todos os restaurantes após essas operações.
