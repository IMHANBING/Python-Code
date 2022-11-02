#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 08:33:31 2022

@author: iris
"""

name = input('输入姓名：')
print('姓名：%s' % name)

print('-' * 20)

QQ = input('输入QQ：')
print('QQ：%s' % QQ)

print('-' * 20)

age = input('输入年龄：')
print('年龄：%d' % int(age))

print('-' * 20)

print('姓名：%s，QQ：%s，年龄：%d' % (name, QQ, int(age)))
