from time_data import Time

class Activity:
    def __init__(self, name, start_time, end_time):
        self.name = name
        self.time = Time(start_time, end_time)

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def serialize(self):
        return {
            "Activity" : self.name,
            "Time" : self.time.serialize()
        }
    # def get_start_time(self):
    #     return self.start_time


    # def get_end_time(self):
    #     return self.end_time


    # def set_end_time(self, end_time):
    #     self.end_time = end_time
    

    # def get_total_time(self):
    #     return self.end_time - self.start_time
