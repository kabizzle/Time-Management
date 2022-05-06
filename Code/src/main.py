import sys
# from file_data import FileData
# from activity import Activity
# from time_data import Time
from PyQt5 import QtWidgets
from gui import GUI

def main():
    # global app
    
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()