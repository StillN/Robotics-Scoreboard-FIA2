import time
from timeit import repeat
from tkinter import Spinbox
from threading import Timer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtCore
from PyQt6 import QtCore, QtGui, QtWidgets
from Final_Scoreboard import Ui_MainWindow
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


class MainWindow:
    team_1_point = 0
    team_2_point = 0
    timers = 60
    

    def __init__(self):
        
        self.widget_counter_int = 0
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        

        self.show()

    def show (self):
        self.MainWindow.show()

    
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())

