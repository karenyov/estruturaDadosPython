# -*- coding: utf-8 -*-
"""Fila circular.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18tBNYWBR03TQl2WMeWsFLQAMpPI-W9Fz

# Fila circular
"""

import numpy as np

class FilaCircular:

  def __init__(self, capacidade):
    self.capacidade = capacidade
    self.inicio = 0
    self.final = -1
    self.numero_elementos = 0
    self.valores = np.empty(self.capacidade, dtype=int)

  def __fila_vazia(self):
    return self.numero_elementos == 0

  def __fila_cheia(self):
    return self.numero_elementos == self.capacidade

  def enfileirar(self, valor):
    if self.__fila_cheia():
      print('A fila está cheia')
      return

    if self.final == self.capacidade - 1:
      self.final = -1
    self.final += 1
    self.valores[self.final] = valor
    self.numero_elementos += 1

  def desenfileirar(self):
    if self.__fila_vazia():
      print('A fila já está vazia')
      return

    temp = self.valores[self.inicio]
    self.inicio += 1
    #if self.inicio == self.capacidade - 1: Corrigido em 05/05/2022
    if self.inicio == self.capacidade:
      self.inicio = 0
    self.numero_elementos -= 1
    return temp

  def primeiro(self):
    if self.__fila_vazia():
      return -1
    return self.valores[self.inicio]

fila = FilaCircular(5)

fila.primeiro()

# 1
fila.enfileirar(1)
fila.primeiro()

# 2 1
fila.enfileirar(2)
fila.primeiro()

# 5 4 3 2 1
fila.enfileirar(3)
fila.enfileirar(4)
fila.enfileirar(5)

fila.enfileirar(6)

# 5 4 3
fila.desenfileirar()
fila.desenfileirar()
fila.primeiro()

# 7 6 5 4 3
fila.enfileirar(6)
fila.enfileirar(7)

fila.primeiro()

fila.valores

fila.inicio, fila.final

fila.valores[fila.final]

fila.valores[fila.inicio]