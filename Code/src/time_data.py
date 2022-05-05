class Time:
    def __init__(self, time):
        self.time = time  # total time in seconds
        self.hours, self.minutes, self.seconds = self.calculate_time()

    def calculate_time(self):
        total_seconds = self.time
        self.hours = total_seconds // 3600
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

        return self.hours, self.minutes, self.seconds

    def get_total_time(self):
        return self.time.seconds
    
    def serialize(self):
        return {
            "hours" : self.hours,
            "minutes" : self.minutes,
            "seconds" : self.seconds
        }
