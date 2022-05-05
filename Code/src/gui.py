from PyQt5 import QtWidgets, QtGui, QtCore
import sys
# from timer_class import Timer

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,625)
        self.setWindowTitle("Time Management")
        self.layout = QtWidgets.QGridLayout(self)
        self.activity_count = 0
        self.timer_count = 0
        self.flag = False

        self.activity_layout = QtWidgets.QVBoxLayout()
        self.button_layout = QtWidgets.QVBoxLayout()
        self.timer_layout = QtWidgets.QVBoxLayout()

        # self.activity_layout.setSizeConstraint(200)

        self.ui_components()
        self.init_buttons()
        self.display_time()
        
        self.layout.addLayout(self.activity_layout,0,0,2,1)
        self.layout.addLayout(self.button_layout,0,2,2,1)
        self.layout.addLayout(self.timer_layout,1,1,2,1)
        self.layout.setSpacing(200)

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,2)
        self.layout.setColumnStretch(2,1)

        self.layout.setHorizontalSpacing(125)
        self.layout.setVerticalSpacing(100)

        # self.activity_layout.setContentsMargins(20, 20, 20, 20) 
        # self.activity_layout.addSpacing(100)       

        # self.add_activity()
        # self.check_buttons()

        # self.setLayout(self.layout)

        self.timer = QtCore.QTimer(self)

		# adding action to timer
        self.timer.timeout.connect(self.display_time)

		# update the timer every second
        self.timer.start(1000)

        self.show()


    def ui_components(self):
        #displaying text
        self.text_label = QtWidgets.QLabel("Your Activities", self)
        # self.text_label.setText("Your Activities")
        # self.text_label.setGeometry(75, 50, 250, 70)
        self.text_label.setFont(QtGui.QFont("Montserrat", 16))
        self.activity_layout.addWidget(self.text_label)


        # textbox to add activities
        self.activity_name = QtWidgets.QLineEdit(self)
        # activity_name.setText("Enter activity name")
        # self.activity_name.setGeometry(75, 30, 20, 35)
        self.activity_name.setFont(QtGui.QFont("Montserrat", 12))
        self.activity_layout.addWidget(self.activity_name)


    def init_buttons(self):
        #creating buttons
        self.add_new = QtWidgets.QPushButton("add new", self, clicked=lambda:self.add_activity(self.activity_count))
        # self.add_new.pressed.connect(lambda:self.add_activity())

        self.next_day = QtWidgets.QPushButton("Next day", self)
        
        self.today_times = QtWidgets.QPushButton("Show today's times", self)
        
        self.past_times = QtWidgets.QPushButton("Show past times", self)
        
        self.read_file = QtWidgets.QPushButton("Read file", self)
        
        self.start_timer = QtWidgets.QPushButton("Start Timer", self, clicked=lambda:self.start())

        self.stop_timer = QtWidgets.QPushButton("Stop Timer", self, clicked=lambda:self.stop())
        
        self.reset_timer = QtWidgets.QPushButton("Reset Timer", self, clicked=lambda:self.reset())

        self.time = QtWidgets.QLCDNumber(self)
        self.timer_layout.addWidget(self.time)
        self.timer_layout.insertSpacing(1, 100)
        self.timer_layout.addSpacing(100)


        #styling buttons
        # self.add_new.setGeometry(350, 300, 150, 37)
        self.add_new.setFont(QtGui.QFont("Montserrat", 12))
        self.activity_layout.addWidget(self.add_new)
        self.activity_layout.insertSpacing(2, 10)


        # self.next_day.setGeometry(750, 100, 200, 40)
        self.next_day.setFont(QtGui.QFont("Montserrat", 12))
        self.button_layout.addWidget(self.next_day)

        # self.today_times.setGeometry(750, 175, 200, 40)
        self.today_times.setFont(QtGui.QFont("Montserrat", 12))
        self.button_layout.addWidget(self.today_times)
        
        # self.past_times.setGeometry(750, 250, 200, 40)
        self.past_times.setFont(QtGui.QFont("Montserrat", 12))
        self.button_layout.addWidget(self.past_times)

        # self.read_file.setGeometry(750, 325, 200, 40)
        self.read_file.setFont(QtGui.QFont("Montserrat", 12))
        self.button_layout.addWidget(self.read_file)

        # self.start_timer.setGeometry(250, 400, 200, 40)
        self.start_timer.setFont(QtGui.QFont("Montserrat", 12))
        self.timer_layout.addWidget(self.start_timer)

        self.stop_timer.setFont(QtGui.QFont("Montserrat", 12))
        self.timer_layout.addWidget(self.stop_timer)

        self.reset_timer.setFont(QtGui.QFont("Montserrat", 12))
        self.timer_layout.addWidget(self.reset_timer)

    def add_activity(self, i):
        # checking that only 5 activities are added
        if i < 5 and self.activity_name.text() != "":
            # checkbox with activities
            text = self.activity_name.text().split("/ ")
            name = text[0]
            hours = text[1]
            # self.activities.addItem(name)
            self.checkbox = QtWidgets.QCheckBox(name, self)
            self.checkbox.setGeometry(25, 100, 30, 30)
            self.checkbox.setFont(QtGui.QFont("Montserrat", 12))

            # layout = QtWidgets.QVBoxLayout(self)
            self.activity_layout.insertWidget(i+1, self.checkbox)
            self.activity_count += 1

        self.activity_name.setText("")

    def display_time(self):        
        if self.flag:   # checking if flag is true  
            self.timer_count += 1  # incrementing the counter
        
        minutes = self.timer_count // 60
        seconds = self.timer_count % 60
        text = f"{minutes}:{seconds:02d}"     # getting text from count
        self.time.display(text)    # showing text

    def start(self):
        self.flag = True

    def stop(self):
        self.flag = False   # making flag to false
    
    def reset(self):
        self.flag = False
        self.timer_count = 0      # resetting the count
    
    def pomodoro(self):
        pass
    

app = QtWidgets.QApplication(sys.argv)
window = GUI()
sys.exit(app.exec_())