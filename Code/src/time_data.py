from datetime import datetime

class Time:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.time, self.hours, self.minutes, self.seconds = self.calculate_time()

    def calculate_time(self):
        self.time = self.end_time - self.start_time
        total_seconds = self.time.seconds
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

        return self.time, self.hours, self.minutes, self.seconds

    def get_total_time(self):
        return self.time.seconds
    
    def serialize(self):
        return {
            "start_time" : self.start_time.isoformat(),
            "end_time" : self.end_time.isoformat(),
            "hours" : self.hours,
            "minutes" : self.minutes,
            "seconds" : self.seconds
        }
