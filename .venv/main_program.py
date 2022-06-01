import time
from timeit import repeat
from tkinter import Spinbox
from threading import Timer
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtGui, QtCore
from PyQt6 import QtCore, QtGui, QtWidgets
from UI import Ui_MainWindow
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
        self.Ui_MainWindow.show()

    
        self.display_gallows()
        
    def signals(self):
        self.signals()
        
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
        
        
        # Saving to File
        self.ui.pushButton_10.clicked.connect(self.save_data)
        self.ui.pushButton_11.clicked.connect(self.save_data)
def display_gallows(self):
        MBC_file_name = (f"./MBC_Logo_T1.png")
        gallow = QPixmap(MBC_file_name)
        self.ui.gallow_lb.setPixmap(gallow)
        
        MBBC_file_name = (f"./MBBC_Logo_T1.png")
        gallow = QPixmap(MBBC_file_name)
        self.ui.gallow_lb_2.setPixmap(gallow)
        
        
    # Team 1 Buttons
        def point_btn_1(self):
            team1_point = MainWindow.team_1_point
            team1_point += 1
            MainWindow.team_1_point += 1
            
        def remove_point_button_1(self):
            team1_point = MainWindow.team_1_point
            team1_point -= 1
            MainWindow.team_1_point -= 1
            
        
        # Team 2 Buttons   
        def point_btn_2(self):
            team2_point = MainWindow.team_2_point
            team2_point += 1
            self.ui.label
            
        def remove_point_button_2(self):
            team2_point = MainWindow.team_2_point
            team2_point -= 1
            MainWindow.team_2_point -= 1

        def reset_points_team_1(self):
            MainWindow.team_1_point = 0
            
        def reset_points_team_2(self):
            MainWindow.team_2_point = 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())

