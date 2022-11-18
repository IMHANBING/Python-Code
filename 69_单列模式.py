# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:37:15 2022

@author: Lenovo
"""


class Dog(object):
    __instance = None
    __init_flat = False

    def __new__(cls, new_name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, new_name):
        if Dog.__init_flat == False:
            self.name = new_name
            Dog.__init_flat = True


a = Dog('旺财')
b = Dog('小白')
print(id(a) == id(b))
print(a.name)
print(b.name)
