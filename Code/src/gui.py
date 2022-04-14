from PyQt5 import QtWidgets, QtGui

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,900,600)
        self.setWindowTitle("Time Management")
        self.setLayout(QtWidgets.QGridLayout())

        appLabel = QtWidgets.QLabel()
        appLabel.setText("Your Activities")
        appLabel.setFont(QtGui.QFont("Montserrat", 16))

        self.init_buttons()

        self.show()

    def init_buttons(self):
        add_new = QtWidgets.QPushButton("add new")
        next_day = QtWidgets.QPushButton("Next Day")
        today_times = QtWidgets.QPushButton("Show today's times")
        past_times = QtWidgets.QPushButton("Show past times")
        read_file = QtWidgets.QPushButton("Read file")
        start_timer = QtWidgets.QPushButton("Start Timer")

        # self.layout().addWidget(add_new, 2, 2, 1, 2)
        # self.layout().addWidget(next_day, 0, 4, 2, 4)
        # self.layout().addWidget(today_times, 1, 4, 2, 4)
        # self.layout().addWidget(past_times, 2, 4, 2, 4)
        # self.layout().addWidget(read_file, 3, 4, 2, 4)
        self.layout().addWidget(start_timer, 4, 4, 2, 4)
