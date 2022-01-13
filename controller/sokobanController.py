from PyQt5.QtCore import right,Qt
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtWidgets import QLabel
from view.sokobanView import SokobanView
from model.sokobanModel import SokobanModel
from PyQt5 import Qt


class SokobanController:
    """
    TODO
    """

    def __init__(self):
        """
        TODO
        """
        self.__model = None
        self.__view = None
        

    def setModel(self, model):
        """
        TODO
        """
        self.__model = model

    def setView(self, view):
        """
        TODO
        """
        self.__view = view


    def restartGame(self):
        """
        TODO
        """
        self.__model.clear()
        self.__view.cleanView()
        self.__model.setPlayerPos((2,2))
        self.__view.updateView()


    def move(self,event):
        """
        TODO
        """
        x,y= event
        a,b=self.__model.getPlayerPos()
        self.__stockCoord=(x+a,y+b)
        if self.__model.get(self.__stockCoord[0],self.__stockCoord[1]) != 1 :
            if self.__model.get(self.__stockCoord[0],self.__stockCoord[1]) != 3 and self.__model.get(self.__stockCoord[0],self.__stockCoord[1]) != 5:
                self.__model.setPlayerPos(self.__stockCoord)
                self.__view.addNbPas()
                
                
            elif self.__model.get(self.__stockCoord[0],self.__stockCoord[1]) == 3 or self.__model.get(self.__stockCoord[0],self.__stockCoord[1]) == 5:
                if  self.__model.get(self.__stockCoord[0]+x,self.__stockCoord[1]+y) != 3 and self.__model.get(self.__stockCoord[0]+x,self.__stockCoord[1]+y) != 1 and self.__model.get(self.__stockCoord[0]+x,self.__stockCoord[1]+y) != 5:                        
                    if self.__model.get(self.__stockCoord[0]+x,self.__stockCoord[1]+y) != 4:
                        self.__model.setPlayerPos(self.__stockCoord)
                        self.__model.set(self.__stockCoord[0],self.__stockCoord[1],2)
                        self.__model.set(self.__stockCoord[0]+x,self.__stockCoord[1]+y,3)
                        self.__view.addNbPas() 
                    else:
                        self.__model.setPlayerPos(self.__stockCoord)
                        self.__model.set(self.__stockCoord[0],self.__stockCoord[1],2)
                        self.__model.set(self.__stockCoord[0]+x,self.__stockCoord[1]+y,5)
                        self.__view.addNbPas() 

                    
        if self.__model.getLevel()==1:
            if self.__model.get(2,1) !=5:
                self.__model.set(2,1,4)
            if self.__model.get(4,1) != 5:
                self.__model.set(4,1,4)
            if self.__model.get(3,5) !=5:
                self.__model.set(3,5,4)
            if self.__model.get(5,4) !=5:
                self.__model.set(5,4,4)
            if self.__model.get(6,6) !=5:
                self.__model.set(6,6,4)
            if self.__model.get(7,4) !=5:
                self.__model.set(7,4,4)
            if self.__model.get(6,3) !=5:
                self.__model.set(6,3,4)
            
            if  self.__model.get(2,1)== 5 and self.__model.get(4,1) == 5 and self.__model.get(3,5)== 5 and self.__model.get(5,4)== 5 and self.__model.get(6,6)== 5 and self.__model.get(7,4)== 5 and self.__model.get(6,3) == 5:
                self.__view.victoire()
        else:
            if self.__model.get(6,19) !=5:
                self.__model.set(6,19,4)
            if self.__model.get(7,19) != 5:
                self.__model.set(7,19,4)
            if self.__model.get(8,19) !=5:
                self.__model.set(8,19,4)
            if self.__model.get(6,20) !=5:
                self.__model.set(6,20,4)
            if self.__model.get(7,20) !=5:
                self.__model.set(7,20,4)
            if self.__model.get(8,20) !=5:
                self.__model.set(8,20,4)
           
            if  self.__model.get(6,19)== 5 and self.__model.get(7,19)== 5 and self.__model.get(8,19)== 5 and self.__model.get(6,20)== 5 and self.__model.get(7,20)== 5 and self.__model.get(8,20)  == 5:
                self.__view.victoire()


        self.__view.updateView()




