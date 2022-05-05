import sys

from time import time
from file_data import FileData
from activity import Activity
from time_data import Time
from PyQt5 import QtWidgets, QtGui
from datetime import datetime
from PyQt5.QtCore import QTimer
import json

from gui import GUI

def main():
    # global app
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()

    # activities = []
    # while True:
    #     activities = time_activity(activities)
    #     exit = input("Would you like to exit or start a new activity? \nType 'e' to exit or 'n' for new activity \n")
    #     while exit.lower() != "e" and exit.lower() != "n":
    #         print("Invalid input")
    #         exit = input("Would you like to exit or start a new activity? \nType 'e' to exit or 'n' for new activity \n")

    #     if exit.lower() == "e":
    #         break
    #     else:
    #         continue

    sys.exit(app.exec_())
    


if __name__ == '__main__':
    main()