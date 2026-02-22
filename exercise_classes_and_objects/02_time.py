class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds : int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> str:
        return (f"{0 if self.hours <= 9 else ''}{self.hours}:{0 if self.minutes <= 1 else ''}{self.minutes}:"
                f"{0 if self.seconds <= 1 else ''}{self.seconds}")

    def next_second(self):
        if self.seconds < self.max_seconds:
            self.seconds += 1
        else:
            self.seconds = 00
            if self.minutes < self.max_minutes:
                self.minutes += 1
            else:
                self.minutes = 00
                if self.hours < self.max_hours:
                    self.hours += 1
                else:
                    self.hours = 00
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
