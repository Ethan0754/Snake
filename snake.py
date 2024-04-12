# -*- coding: utf-8 -*-

from graphics import *
import time
"""
Created on Fri Apr 12 11:17:29 2024

@author: Ethan
"""



def getDirection(direction):
    press = win.checkKey()
    if press == "w":
        direction = "w"
    if press == "s":
        direction = "s"
    if press == "a" :
        direction = "a"
    if press == "d":
        direction = "d"

    return direction

def apple():
    print("apple")


def draw(direction):
    if(direction == "w"):
        aLine.move(0,-8)
    if(direction == "s"):
        aLine.move(0, 8)
    if(direction == "i"):
        bLine.move(0,-8)
    if(direction == "k"):
        bLine.move(0, 8)
        

def newRect():
    print("newrect")



def main():
    win=GraphWin("Circle", 1000, 700)
    snakeX = [500]
    snakeY = [350]
    
    
    
    
    
    
    
    
