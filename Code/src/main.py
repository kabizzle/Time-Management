from time import time
from file_data import FileData
from activity import Activity
from time_data import Time
from PyQt5 import QtGui, QtWidgets
from datetime import datetime
import json


def main():
    activities = []
    activity_name = input("Enter activity name: \n")
    start_time = datetime.now()
    print(f"{activity_name} started at time {start_time.time()}.")

    while True:
        end = input("Enter 'stop' to end your activity timer: \n")
        if end.lower() == "stop":
            end_time = datetime.now()
            activities.append(Activity(activity_name, start_time, end_time))

            activity = activities[0]

            print(f"{activity.get_name()} ended at time {end_time.time()}.")
            print(f"Total time was {activity.get_time().get_total_time()}")
            time_info = activity.serialize()

            # time_info = {
            # "start_time" : activity.get_start_time().isoformat(),
            # "end_time" : activity.get_end_time().isoformat(),
            # "total_time" : total_time
            # } 

            time_info_json = json.dumps(time_info, indent=4)

            with open('time_data.json', 'r+') as time_file:
                time_file.write(time_info_json)
            
            
            break
    

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


if __name__ == '__main__':
    main()