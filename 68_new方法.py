# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:33:07 2022

@author: Lenovo
"""


class Dog(object):
    def __new__(cls):
        print('new')
        return object.__new__(cls)

    def __init__(self):
        print('init')

    def __str__(self):
        return 'str'

    def __del__(self):
        print('del')


dog = Dog()
print(dog)
