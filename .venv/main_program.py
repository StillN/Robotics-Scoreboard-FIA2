from socket import TIPC_MEDIUM_IMPORTANCE
import time
from timeit import repeat
from tkinter import Spinbox
from threading import Timer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtCore
from PyQt6 import QtCore, QtGui, QtWidgets
from UI_Scoreboard import Ui_MainWindow
from UI_Scoreboard  import * 
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

def __init__(self):
    
    self.time_rem_int = TIME_INT
    self.widget_counter_int = 0
    self.main_win = QMainWindow()
    self.ui = Ui_MainWindow()
    self.ui.setupUI(self.main_win)
    
self.signals()
self.display_gallows()

def show(self):
    self.main_win.show()

def signals(self):
    
# UI Buttons to values
 # Team 1 Buttons
 self.ui.pushButton.clicked.connect(self.point_btn_1)
 self.ui.pushButton_2.clicked.connect(self.remove_point_button_1)

# Team 2 Buttons
 self.ui.pushButton_3.clicked.connect(self.remove_point_button_2)
 self.ui.pushButton_4.clicked.connect(self.point_btn_2)
 
 # Reset Score Buttons
 self.ui.pushButton_5.clicked.connect(self.reset_points_team_1)
 self.ui.pushButton_6.clicked.connect(self.reset_points_team_2)
 
 # Timer Buttons
 self.ui.pushButton_7.clicked.connect(self.add)
 self.ui.pushButton_8.clicked.connect(self.pause_timer)
 self.ui.spinBox.valueChanged.connect(self.spin)
 
 
 # Images Display
 
 def display_gallows(self):
     MBC_file_name = (f"./MBC_Logo_T1.png")
     gallow = QPixmap(MBC_file_name)
     self.ui.gallow_lb.setPixmap(gallow)
     
     MBBC_file_name = (f"./MBBC_Logo_T1.png")
     gallow = QPixmap(MBBC_file_name)
     self.ui.gallow_lb_2.setPixmap(gallow)


# Team 1 Buttons
  

    








if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
