"""
TODO
"""
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QWidget, QPushButton, QMenu, QAction, QDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage, QIcon
from PyQt5.QtCore import QSize, Qt, QDir, QCoreApplication, QUrl, qsrand
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, QSound, QSoundEffect, QAudio


class SokobanView(QMainWindow):
    """
    TODO
    """

    def __init__(self):
        """
        TODO
        """
        super().__init__()

        self.setWindowTitle("Sokoban")
        

        self.__window = QWidget()
        self.setCentralWidget(self.__window)
        self.__gridLayout = QGridLayout()
        self.__window.setLayout(self.__gridLayout)
        self.__gridLabel = []
        self.__gridLabel2 = []
        self.__gridLayout.setSpacing(0)
        self.__gridLayout.setContentsMargins(0,0,0,0)
        self.__model = None
        self.__controller = None
        self.__levelSound = QSound("sound/level1.wav")
        
        self.image=QLabel()
        self.pixmap=QPixmap('images/ali.jpg')
        self.image.setPixmap(self.pixmap)
    

        menuBar = self.menuBar()
        gameMenu = QMenu("&Jeu", self)
        menuBar.addMenu(gameMenu)

        helpMenu = QAction("&Help", self)
        helpMenu.triggered.connect(self.helpView)
        menuBar.addAction(helpMenu)

        restart = QAction(self)
        restart.setText("&Restart")
        gameMenu.addAction(restart)
        restart.triggered.connect(self.restart)

        exitProgram = QAction(self)
        exitProgram.setText("&Quit")
        gameMenu.addAction(exitProgram)
        exitProgram.triggered.connect(self.close)

        nextProgram = QAction(self)
        nextProgram.setText("&Level2")
        gameMenu.addAction(nextProgram)
        nextProgram.triggered.connect(self.test)


        self.__trou = QPixmap.fromImage(QImage("images/trou.png", 'png')).scaled(50, 50)
        self.__perso = QPixmap.fromImage(QImage("images/boxeur.png", 'png')).scaled(58, 58)
        self.__brique = QPixmap.fromImage(QImage("images/brique.png", 'png')).scaled(50, 50)
        self.__sol = QPixmap.fromImage(QImage("images/sol.png", 'png')).scaled(50, 50)
        self.__caisse = QPixmap.fromImage(QImage("images/caisse.png", 'png')).scaled(50, 50)
        self.__vide = QPixmap.fromImage(QImage("images/vide.png", 'png')).scaled(50, 50)
        self.__caissevalide= QPixmap.fromImage(QImage("images/caissevalide.png", 'png')).scaled(50, 50)

        self.__window.setFixedSize(400, 450)




        self.playlist = QMediaPlaylist()
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.levelSound = QMediaPlayer()
        self.levelSound.setPlaylist(self.playlist)

    def test(self):
        self.__model.addLevel()

    def helpView(self):
        """
        TODO
        """
        dialog = QDialog()
        dialog.setAttribute(Qt.WA_DeleteOnClose)
        dialog.setWindowTitle("Help")

        label = QLabel("<h1> J'ai besoin d'aide </h1>", parent=dialog)
        label.show()
        dialog.exec_()

    def victoire(self):
        self.image.show()

    def actionCalled(self, l, c):
        """
        TODO
        """
        self.__controller.play(l, c)

    def setModel(self, model):
        """
        TODO
        """
        self.__window.setFixedSize(400, 450)
        self.__model = model
        self.__levelSound.play()
        for i in range(len(self.__model.getMatrix())):
            tmp = []
            for j in range(len(self.__model.getMatrix()[0])):
                label = QLabel(parent=self.__window)
                tmp.append(label)
                self.__gridLayout.addWidget(label, i, j)

            self.__gridLabel.append(tmp)

        for i in range(len(self.__model.getMatrix())):
            tmp = []
            for j in range(len(self.__model.getMatrix()[0])):
                label = QLabel(parent=self.__window)
                tmp.append(label)
                self.__gridLayout.addWidget(label, i, j)
             

            self.__gridLabel2.append(tmp)
        if self.__model.getLevel() == 1:
            self.__window.setFixedSize(400, 450)
        if self.__model.getLevel() == 2:
            self.__window.setFixedSize(1100, 550)
        if self.__model.getLevel() == 3:
            self.__window.setFixedSize(1100, 650)
        
        self.updateView()
        
        


    def cleanView(self):
        """
        TODO
        """
        for llabel in self.__gridLabel:
            for label in llabel:
                label.setPixmap(QPixmap())

        for llabel in self.__gridLabel2:
            for label in llabel:
                label.setPixmap(QPixmap())

    def restart(self):
        """
        TODO
        """
        self.__controller.restartGame()
       
        

    def setController(self, controller):
        """
        TODO
        """
        self.__controller = controller


    def addNbPas(self):
        """
        TODO
        """
        self.__model.setNbPas(self.__model.getNbPas()+ 1)
        self.statusBar().showMessage("Le nombre de pas est : {} ".format(self.__model.getNbPas()))
        
       
    def view2(self):
        self.view=SokobanView()
        self.view.setController(self.__controller)
        self.view.setModel(self.__model)
        self.__controller.setView(self.view)
        self.__model.addView(self.view)
        self.view.show()
        self.close()
        

    def updateView(self):
        """
        TODO
        """
        
        for i in range(len(self.__model.getMatrix())):
            for j in range(len(self.__model.getMatrix()[0])):
                tmp=self.__model.get(i,j)
                label = self.__gridLabel[i][j]
                if tmp == 1:
                    label.setPixmap(self.__brique)
                elif tmp == 2:
                    label.setPixmap(self.__sol)
                elif tmp == 3:
                    label.setPixmap(self.__caisse)
                elif tmp == 4:
                    label.setPixmap(self.__trou)
                elif tmp == 0:
                    label.setPixmap(self.__vide)
                elif tmp == 5:
                    label.setPixmap(self.__caissevalide)

        for i in range(len(self.__model.getMatrix())):
            for j in range(len(self.__model.getMatrix()[0])):
                label = self.__gridLabel2[i][j]
                if self.__model.getPlayerPos() == (i,j):
                    label.setPixmap(self.__perso)
                else: label.setPixmap(QPixmap())

    def keyPressEvent(self, event):
        """
        Cet event s'active à chaque touche appuyé
        Les touches q et fleche de Gauche font aller le personnage à gauche
        Les touches d et fleche de Droite font aller le personnage à droite
        Les touches z et fleche de Haut font aller le personnage à haut
        Les touches s et fleche de Bas font aller le personnage à bas
        """
        key = event.key()
        if key == Qt.Key_Left or key == Qt.Key_Q:
            self.__controller.move((0,-1))
            print("Left")
        elif key == Qt.Key_Right or key == Qt.Key_D:
            self.__controller.move((0,1))
            print("Right")
        elif key == Qt.Key_Up or key == Qt.Key_Z:
            self.__controller.move((-1,0))
            print("Up")
        elif key == Qt.Key_Down or key == Qt.Key_S:
            self.__controller.move((1,0))
            print("Down")
        else:
            super(SokobanView, self).keyPressEvent(event)