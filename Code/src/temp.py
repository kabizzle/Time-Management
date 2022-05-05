# from time import time
# from file_data import FileData
from activity import Activity
# from time_data import Time
import json
from datetime import datetime


def activity_in_list(activities, name):
    for activity in activities:
        if activity.get_name() == name:
            return activity
        else:
            return None


def time_activity(activities):
    activity_name = input("Enter activity name: \n")
    text = activity_name.split("/")
    name = text[0]
    hours = text[1]
    start_time = datetime.now()
    print(f"{name} started at time {start_time.time()}.")

    while True:
        end = input("Enter 'stop' to end your activity timer: \n")
        if end.lower() == "stop":
            end_time = datetime.now()
            activity = activity_in_list(activities, activity_name)
            if activity:
                activity.change_time(start_time, end_time)
            else:
                activities.append(Activity(name, start_time, end_time, hours))
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
    activities = []
    while True:
        activities = time_activity(activities)
        exit = input("Would you like to exit or start a new activity? \nType 'e' to exit or 'n' for new activity \n")
        while exit.lower() != "e" and exit.lower() != "n":
            print("Invalid input")
            exit = input("Would you like to exit or start a new activity? \nType 'e' to exit or 'n' for new activity \n")

        if exit.lower() == "e":
            break
        # else:
        #     continue


if __name__ == "__main__":
    main()