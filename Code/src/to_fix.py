from datetime import datetime
import json

# input activity name

# when "start timer" is clicked 
start_time = datetime.now()

# when "reset timer" is clicked
end_time = datetime.now()
activity = activity_in_list(activities, activity_name)
if activity:
    activity.change_time(start_time, end_time)
else:
    activities.append(Activity(activity_name, start_time, end_time))
    i = len(activities) - 1
    activity = activities[i]

# Maybe print these in a dialogue window:
# # print(f"\n{activity.get_name()} ended at time {end_time.time()}.")
# # print(f"Total time was {activity.get_time().get_total_time()}\n")
time_info = activity.serialize()

time_info_json = json.dumps(time_info, indent=4)

with open('time_data.json', 'a+') as time_file:
    time_file.write(time_info_json)

#*************************************************************************************************************************#

def activity_in_list(activities, name):
    for activity in activities:
        if activity.get_name() == name:
            return activity
        else:
            return None

def start_time():
    start_time = datetime.now()

def time_activity(activities):
    # activity_name = get from text box
    end_time = datetime.now()
    activity = activity_in_list(activities, activity_name)
    if activity:
        activity.change_time(start_time, end_time)
    else:
        activities.append(Activity(activity_name, start_time, end_time))
        i = len(activities) - 1
        activity = activities[i]

    time_info = activity.serialize()

    time_info_json = json.dumps(time_info, indent=4)

    with open('time_data.json', 'a+') as time_file:
        time_file.write(time_info_json)
    return activities    
