#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    lista_produtos = []

    def __init__(self, id='', nome=''):
        self.produto_id = id
        self.produto_nome = nome
        __class__.lista_produtos.append(self)

    def set_id(self, new_id):
        self.produto_id = new_id

    def get_id(self):
        return self.produto_id

    @classmethod
    def busca_nome(cls, nome):
        lista_pesquisa = []
        for produto in Produto.lista_produtos:
            if produto.produto_nome[0:len(nome)].lower() == nome.lower():
                lista_pesquisa.append(produto)
        return lista_pesquisa