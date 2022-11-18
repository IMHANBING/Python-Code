# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:21:24 2022

@author: Lenovo
"""


class Game(object):
    num = 0  # 类属性

    def __init__(self):  # 实例方法
        self.name = '老王'  # 实例属性

    @classmethod
    def add_num(cls):  # 类方法
        cls.num = 100  # 类属性

    @staticmethod
    def print_menu():  # 静态方法，可以没有参数，功能独立
        print('=' * 20)
        print('游戏开始')
        print('=' * 20)


game = Game()
print(game.name)
Game.add_num()
print(Game.num)
game.add_num()
print(game.num)
Game.print_menu()
game.print_menu()
