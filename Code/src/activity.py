from time_data import Time

class Activity:
    def __init__(self, name, total):
        self.name = name
        self.times = []
        self.required = int(total) # in hours
        self.total = 0

    def get_name(self):
        return self.name

    def get_total_time(self):
        return self.total / 3600

    def add_time(self, time):  # time in seconds
        self.times.append(Time(time))
        self.total += time
    
    def calculate_progress(self):
        progress = self.total / (self.required*3600)
        return progress*100

    def serialize_times(self):
        times = {}
        count = 1
        for time in self.times:
            times[f"Entry {count}"] = time.serialize()
            count += 1
        
        return times
    
    def serialize(self):
        return {
            "Activity" : self.name,
            "Times" : self.serialize_times(),
            "Progress" : f"{self.calculate_progress():.02f}%"
        }
