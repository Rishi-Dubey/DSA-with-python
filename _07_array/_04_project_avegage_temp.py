# program that will store ask for days and ask for temp on those days and gives the avg .


class temperature:
    def __init__(self):
        self.high_temp: list = []
        self.total_days: int = self.day_record()

        # update the temp in self.high_temp list
        self.temp_record(self.total_days)
        
        # printing avg temperature
        self.average()
        

    def day_record(self) -> int:
        while True:
            days = input("How many days ? ")
            if days.isdigit() and float(days).is_integer() and int(days) > 0:
                return int(days)

            print("Invalid input ):\n")

    def temp_record(self, days) -> None:
        for i in range(days):
            while True:
                days_temp = input(f"High temperature of day({i + 1}) : ")

                if days_temp.isdigit() and float(days_temp).is_integer():
                    self.high_temp.append(int(days_temp))
                    break

                print("Invalid input ):\n")

    def average(self):
        
        self.avg = round(sum(self.high_temp) / self.total_days, 2)
        print(f"\nAvg temp : {self.avg}")
        
        # count of days in which temp is higher than avg
        count = 0
        for i in self.high_temp:
            if self.avg > i:
                count += 1
        
        print(f"{count} day(s) have higher temp than Avg temp")
user = temperature()

