# coding: utf-8
# license: GPLv3
from gameunit import *
class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._attack = 50
        self._opit = 0
        self._name = name
    def attack(self, target):
        self._health -= target
        return self._health
    def get_helth(self):
        return self._health
    def get_opit(self):
        return self._opit


#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

""" 