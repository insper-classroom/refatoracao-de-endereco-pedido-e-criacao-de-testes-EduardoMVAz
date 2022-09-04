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
        
        if isinstance(id, int) or isinstance(id, str):
            self.produto_id = id
        else:
            raise TypeError

        if isinstance(nome, str):
            self.produto_nome = nome
        else:
            raise TypeError

        __class__.lista_produtos.append(self)

    def set_id(self, new_id):
        if isinstance(id, int):
            self.produto_id = new_id
        else:
            raise TypeError

    def get_id(self):
        return self.produto_id

    def busca_nome(nome):
        lista_pesquisa = []
        for produto in Produto.lista_produtos:
            if produto.produto_nome[0:len(nome)].lower() == nome.lower():
                lista_pesquisa.append(produto)
        if len(lista_pesquisa) > 0:
            return lista_pesquisa
        else:
            return 'Esse produto não existe!'