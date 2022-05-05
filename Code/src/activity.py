from time_data import Time

class Activity:
    def __init__(self, name, start_time, end_time, total):
        self.name = name
        self.time = Time(start_time, end_time)
        self.required = total * 3600 # in seconds
        self.total = 0

    def get_name(self):
        return self.name

    def get_time(self):
        return self.time

    def change_time(self, start_time, end_time):
        self.time = Time(start_time, end_time)
        self.update_total(self.time.get_total_time())
    
    def calculate_progress(self):
        progress = self.time.get_total_time() / self.required
        return progress*100
    
    def update_total(self, added_time):
        self.total += added_time

    def serialize(self):
        return {
            "Activity" : self.name,
            "Time" : self.time.serialize(),
            "Progress" : f"{self.calculate_progress():02.0f}%"
        }
    # def get_start_time(self):
    #     return self.start_time


    # def get_end_time(self):
    #     return self.end_time


    # def set_end_time(self, end_time):
    #     self.end_time = end_time
    

    # def get_total_time(self):
    #     return self.end_time - self.start_time
