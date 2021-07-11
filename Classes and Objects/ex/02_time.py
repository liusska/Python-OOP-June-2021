class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        display_hours = self.hours
        display_minutes = self.minutes
        display_second = self.seconds
        if display_second < 10:
            display_second = f'0{display_second}'
        if display_minutes < 10:
            display_minutes = f'0{display_minutes}'
        if display_hours < 10:
            display_hours = f'0{display_hours}'
        return f"{display_hours}:{display_minutes}:{display_second}"

    def next_second(self):
        if self.seconds < Time.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 0
            if self.minutes < Time.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 0
                if self.hours < Time.max_hours:
                    self.hours += 1
                else:
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
