#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from typing import Type
from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.itens = {}

    def adicionar_item(self, item:Produto, qtd=1):
        
        id = item.get_id()
        if not isinstance(qtd, int):
            raise TypeError

        if item in self.itens:
            self.itens[item] += qtd
        else:
            self.itens[item] = qtd
        
        # Implemente a adição do item no dicionário - Feito
        
    def altera_quantidade(self, item:Produto, qtd):
        if item in self.itens:
            self.itens[item] = qtd
        else:
            return 'Esse Item não existe!'
        

    def remover_item(self, item:Produto):
        if item in self.itens:
            del self.itens[item]
        else:
            return 'Esse Item não existe!'
        # Implemente este método - Feito
