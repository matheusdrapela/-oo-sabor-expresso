from modelos.restaurante import Restaurante
from modelos.cardapio.pratos import Prato
from modelos.cardapio.bebidas import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida ('Suco de Melancia', 5.0, 'grande')
bebida_suco.obter_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.obter_desconto()
restaurante_praca.adicionar_ao_cardapio(bebida_suco)
restaurante_praca.adicionar_ao_cardapio(prato_paozinho)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()