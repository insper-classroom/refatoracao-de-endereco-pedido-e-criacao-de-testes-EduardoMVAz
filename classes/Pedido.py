#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:

    EM_ABERTO = 1
    PAGO = 2

    def __init__(self, cliente:PessoaFisica, carrinho:Carrinho):
        self.cliente = cliente
        self.carrinho = carrinho
        self.endereco_entrega = ''
        self.endereco_faturamento = ''
    
    def __str__(self):
        return str(self.cliente.nome) + ' - ' + str(self.endereco_entrega) + ' - ' + str(self.carrinho.itens)