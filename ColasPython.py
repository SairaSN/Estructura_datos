#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LEE - Sala S - PC 01
#
# Created:     06/04/2022
# Copyright:   (c) LEE - Sala S - PC 01 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Queue:
    def __init__(self):
        self.__items= []

    def enqueue(self, item):
        self.__items.insert(0,item)

    def is_empty(self):
        return not bool (self.__items)

    def dequeue(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)


