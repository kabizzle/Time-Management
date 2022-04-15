from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,750)
        self.setWindowTitle("Time Management")
        # self.setLayout(QtWidgets.QGridLayout())

        self.ui_components()
        self.init_buttons()

        self.show()

    
    def ui_components(self):
        #displaying text
        self.text_label = QtWidgets.QLabel(self)
        self.text_label.setText("Your Activities")
        self.text_label.setGeometry(75, 100, 250, 70)
        self.text_label.setFont(QtGui.QFont("Montserrat", 16))

        # displaying time
        self.time_label = QtWidgets.QLabel(self)
        self.time_label.setGeometry(75, 100, 200, 80)
        self.time_label.setStyleSheet("border : 4px FF0000;")
        self.time_label.setFont(QtGui.QFont("Montserrat", 12))
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)


    def init_buttons(self):
        #creating buttons
        add_new = QtWidgets.QPushButton("add new", self)
        next_day = QtWidgets.QPushButton("Next Day", self)
        today_times = QtWidgets.QPushButton("Show today's times", self)
        past_times = QtWidgets.QPushButton("Show past times", self)
        read_file = QtWidgets.QPushButton("Read file", self)
        start_timer = QtWidgets.QPushButton("Start Timer", self)

        #styling buttons
        add_new.setGeometry(150, 40, 200, 40)
        add_new.setFont(QtGui.QFont("Montserrat", 12))

        next_day.setGeometry(750, 90, 200, 40)
        next_day.setFont(QtGui.QFont("Montserrat", 12))

        today_times.setGeometry(750, 140, 200, 40)
        today_times.setFont(QtGui.QFont("Montserrat", 12))
        
        past_times.setGeometry(750, 190, 200, 40)
        past_times.setFont(QtGui.QFont("Montserrat", 12))

        read_file.setGeometry(750, 240, 200, 40)
        read_file.setFont(QtGui.QFont("Montserrat", 12))

        start_timer.setGeometry(450, 290, 200, 40)
        start_timer.setFont(QtGui.QFont("Montserrat", 12))



app = QtWidgets.QApplication(sys.argv)
window = GUI()
sys.exit(app.exec_())