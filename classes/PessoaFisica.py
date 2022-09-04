#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
import re


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    lista_pessoas = []

    def __init__(self, nome='Visitante', email='', cpf=''):
        
        if not isinstance(nome, str):
            raise TypeError
        else:
            self.nome = nome


        if not isinstance(email, str):
            raise TypeError
        else:
            self.email = email

        if isinstance(cpf, str) or isinstance(cpf, int):
            self.cpf = cpf
        else:
            raise TypeError


        self.enderecos = {}
        __class__.lista_pessoas.append(self)

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_endereco, end:Endereco):
        self.enderecos[apelido_endereco] = end

    def remover_endereco(self, apelido_endereco):
        if apelido_endereco in self.enderecos:
            del self.enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        return self.enderecos[apelido_endereco]

    def listar_enderecos(self):
        return self.enderecos

    def busca_nome(nome):
        lista_pesquisa = []
        for pessoa in PessoaFisica.lista_pessoas:
            if pessoa.nome[0:len(nome)].lower() == nome.lower():
                lista_pesquisa.append(pessoa)
        if len(lista_pesquisa) > 0:
            return lista_pesquisa
        else:
            return 'Nenhum usuário com este nome!'