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

def activity_in_list(activities, name):
    for activity in activities:
        if activity.get_name() == name:
            return activity
        else:
            return None


def time_activity(activities):
    activity_name = input("Enter activity name: \n")
    start_time = datetime.now()
    print(f"{activity_name} started at time {start_time.time()}.")

    while True:
        end = input("Enter 'stop' to end your activity timer: \n")
        if end.lower() == "stop":
            end_time = datetime.now()
            activity = activity_in_list(activities, activity_name)
            if activity:
                activity.change_time(start_time, end_time)
            else:
                activities.append(Activity(activity_name, start_time, end_time))
                i = len(activities) - 1
                activity = activities[i]

            print(f"\n{activity.get_name()} ended at time {end_time.time()}.")
            print(f"Total time was {activity.get_time().get_total_time()}\n")
            time_info = activity.serialize()


            time_info_json = json.dumps(time_info, indent=4)

            with open('time_data.json', 'a+') as time_file:
                time_file.write(time_info_json)
            break
    return activities    


def main():
    # global app
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()

    # window.show()
    # file_data = read_json()

    activities = []
    while True:
        activities = time_activity(activities)
        exit = input("Would you like to exit or start a new activity? \nType 'e' to exit or 'n' for new activity \n")
        while exit.lower() != "e" and exit.lower() != "n":
            print("Invalid input")
            exit = input("Would you like to exit or start a new activity? \nType 'e' to exit or 'n' for new activity \n")

        if exit.lower() == "e":
            break
        else:
            continue

    sys.exit(app.exec_())
    

    # start = datetime(2022, 3, 24, 17, 30, 0)
    # end = datetime.now()
    # total_time = end - start
    # print("start time: ", start.time())
    # print("end time: ", end.time())
    # print("total time: ", total_time)

    # time_info = {
    #     "start_time" : start.isoformat(),
    #     "end_time" : end.isoformat()
    #     # "total_time" : total_time
    # } 

    # time_info_json = json.dumps(time_info, indent=4)

    # with open('Code/src/time_data.json', 'w') as time_file:
    #     time_file.write(time_info_json)

    #     while True:
    #         end = input("Enter 'stop' to end your activity timer: \n")
    #         if end.lower() == "stop":
    #             end_time = datetime.now()
    #             activities.append(Activity(activity_name, start_time, end_time))

    #             activity = activities[i]
    #             i += 1

    #             print(f"\n{activity.get_name()} ended at time {end_time.time()}.")
    #             print(f"Total time was {activity.get_time().get_total_time()}\n")
    #             time_info = activity.serialize()

    #             # time_info = {
    #             # "start_time" : activity.get_start_time().isoformat(),
    #             # "end_time" : activity.get_end_time().isoformat(),
    #             # "total_time" : total_time
    #             # } 

    #             time_info_json = json.dumps(time_info, indent=4)

    #             with open('time_data.json', 'a+') as time_file:
    #                 time_file.write(time_info_json)
                
                
    #             break

            # time_info = {
            # "start_time" : activity.get_start_time().isoformat(),
            # "end_time" : activity.get_end_time().isoformat(),
            # "total_time" : total_time
            # } 


    # window = QtWidgets.QWidget()
    # window.setGeometry(100,100,900,600)
    # window.setWindowTitle("Time Management")
    
    # appLabel = QtWidgets.QLabel(window)
    # appLabel.setText("Your Activities")
    # appLabel.setFont(QtGui.QFont("Montserrat", 16))


if __name__ == '__main__':
    main()