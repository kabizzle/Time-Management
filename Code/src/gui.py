from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from activity import Activity

# from timer_class import Timer

class GUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,1000,625)
        self.setWindowTitle("Time Management")

        self.activities = []
        self.checkboxes = []
        self.timer_count = 0
        self.flag = False

        self.configure_layout()
        self.ui_components()
        self.init_buttons()
        self.display_time()

        self.timer = QtCore.QTimer(self)

		# adding action to timer
        self.timer.timeout.connect(self.display_time)

		# update the timer every second
        self.timer.start(1000)

        self.show()

    def configure_layout(self):
        self.layout = QtWidgets.QGridLayout(self)

        self.activity_layout = QtWidgets.QVBoxLayout()
        self.button_layout = QtWidgets.QVBoxLayout()
        self.timer_layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.activity_layout,0,0,2,1)
        self.layout.addLayout(self.button_layout,0,2,2,1)
        self.layout.addLayout(self.timer_layout,1,1,2,1)
        self.layout.setSpacing(200)

        self.layout.setColumnStretch(0,1)
        self.layout.setColumnStretch(1,2)
        self.layout.setColumnStretch(2,1)

        self.layout.setHorizontalSpacing(125)
        self.layout.setVerticalSpacing(100)

    def ui_components(self):
        #displaying text
        self.text_label = QtWidgets.QLabel("Your Activities", self)
        self.text_label.setFont(QtGui.QFont("Montserrat", 16))
        self.activity_layout.addWidget(self.text_label)

        # textbox to add activities
        self.activity_name = QtWidgets.QLineEdit(self)
        self.activity_name.setFont(QtGui.QFont("Montserrat", 12))
        self.activity_layout.addWidget(self.activity_name)

        # textbox for filename
        self.file_input = QtWidgets.QLineEdit(self)
        self.file_input.setFont(QtGui.QFont("Montserrat", 12))

    def init_buttons(self):
        # creating buttons
        self.add_new = QtWidgets.QPushButton("add new", self, clicked=lambda:self.add_activity())
        self.next_day = QtWidgets.QPushButton("Next day", self, clicked=lambda:self.next())
        self.today_times = QtWidgets.QPushButton("Show today's times", self)
        self.past_times = QtWidgets.QPushButton("Show past times", self)
        self.read_file = QtWidgets.QPushButton("Read file", self)
        self.start_timer = QtWidgets.QPushButton("Start Timer", self, clicked=lambda:self.start())
        self.stop_timer = QtWidgets.QPushButton("Stop Timer", self, clicked=lambda:self.stop())
        self.reset_timer = QtWidgets.QPushButton("Reset Timer", self, clicked=lambda:self.reset())

        # creating time display
        self.time = QtWidgets.QLCDNumber(self)
        self.timer_layout.addWidget(self.time)
        self.timer_layout.insertSpacing(1, 100)
        self.timer_layout.addSpacing(100)

        # styling buttons
        self.add_new.setFont(QtGui.QFont("Montserrat", 12))
        self.activity_layout.insertSpacing(2, 10)
        self.next_day.setFont(QtGui.QFont("Montserrat", 12))
        self.today_times.setFont(QtGui.QFont("Montserrat", 12))
        self.past_times.setFont(QtGui.QFont("Montserrat", 12))
        self.read_file.setFont(QtGui.QFont("Montserrat", 12))
        self.start_timer.setFont(QtGui.QFont("Montserrat", 12))
        self.stop_timer.setFont(QtGui.QFont("Montserrat", 12))
        self.reset_timer.setFont(QtGui.QFont("Montserrat", 12))

        # adding buttons to layout
        self.activity_layout.addWidget(self.add_new)
        self.button_layout.addWidget(self.next_day)
        self.button_layout.addWidget(self.today_times)
        self.button_layout.addWidget(self.past_times)
        self.button_layout.addWidget(self.file_input)
        self.button_layout.addWidget(self.read_file)
        self.timer_layout.addWidget(self.start_timer)
        self.timer_layout.addWidget(self.stop_timer)
        self.timer_layout.addWidget(self.reset_timer)

    def check_activities(self, name):
        for activity in self.activities:
            if activity.get_name() == name:
                return True
        
        return False

    def add_activity(self):
        if len(self.activities) < 5 and self.activity_name.text():  # checking that only 5 activities are added
            text = self.activity_name.text().split("/")
            name = text[0]
            hours = int(text[1])
            
            if self.check_activities(name):
                print("Activity already exists \n")
            else:
                self.activities.append(Activity(name, hours))  # creating object

            checkbox = QtWidgets.QCheckBox(name, self)
            checkbox.setGeometry(25, 100, 30, 30)
            checkbox.setFont(QtGui.QFont("Montserrat", 12))
            self.activity_layout.insertWidget(len(self.activities), checkbox)

            self.checkboxes.append(checkbox)

        self.activity_name.setText("")

    def add_time(self, time):
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                index = self.checkboxes.index(checkbox)
                activity = self.activities[index]
                activity.add_time(time)

                name = checkbox.text().split(" / ")
                checkbox.setText(f"{name[0]} / {activity.calculate_progress():.02f}%")

    def display_time(self):        
        if self.flag:   # checking if flag is true  
            self.timer_count += 1  # incrementing the counter
        
        minutes = self.timer_count // 60
        seconds = self.timer_count % 60
        text = f"{minutes}:{seconds:02d}"     # getting text from count
        self.time.display(text)    # showing text

    def start(self):
        self.flag = True    # setting flag to True

    def stop(self):
        self.flag = False   # setting flag to False
    
    def reset(self):
        self.flag = False
        self.add_time(self.timer_count)  # adding time to activities selected
        self.timer_count = 0      # resetting the count
    
    def pomodoro(self):
        pass
    
    def next(self):
        pass
    
    def today(self):
        pass

    def past(self):
        pass
    
    def read(self):
        pass

app = QtWidgets.QApplication(sys.argv)
window = GUI()
sys.exit(app.exec_())