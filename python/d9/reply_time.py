from datetime import datetime,timedelta,time


class ReplyTime():
    HOLIDAYS = [
        "01-01",
        "2022-01-03"
    ]
    def  __init__(self,received_time, duration_in_hour,open_business_time,close_business_time):
        self.received_time = received_time
        self.duration_in_hour = duration_in_hour
        self.open_business_time = open_business_time
        self.close_business_time = close_business_time

    def calculate_start_working_time(self):
        start_working_time = self.received_time 
        while ((start_working_time.isoweekday() == 5) and (start_working_time.time() >= self.close_business_time)) \
            or (start_working_time.isoweekday() >= 6) \
            or (start_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (start_working_time.strftime("%m-%d") in self.HOLIDAYS):
            start_working_time = self.received_time + timedelta(days=8-self.received_time.isoweekday())
            start_working_time = start_working_time.replace(
                hour = self.open_business_time.hour,
                minute = 0,
                second = 0,
                microsecond = 0
            )
            if (start_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (start_working_time.strftime("%m-%d") in self.HOLIDAYS):
                start_working_time += timedelta(days=1)

        while (start_working_time.time() >= self.close_business_time) \
            or (start_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (start_working_time.strftime("%m-%d") in self.HOLIDAYS):
            start_working_time = start_working_time.replace(
                day = start_working_time.day + 1,
                hour = self.open_business_time.hour,
                minute = 0,
                second = 0,
                microsecond = 0
            )
        return start_working_time
    
    def calculate_stop_working_time(self,start_working_time):
        stop_working_time = start_working_time + timedelta(hours=self.duration_in_hour)
        if stop_working_time.time() > self.close_business_time:
            close_business_time = stop_working_time.replace(
                hour= self.close_business_time.hour,
                minute=self.close_business_time.minute
            )
            remaining_time = stop_working_time - close_business_time

        while ((stop_working_time.isoweekday() == 5) and (stop_working_time.hour >= self.close_business_time.hour)) \
            or (stop_working_time.isoweekday() >= 6) \
            or (stop_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (stop_working_time.strftime("%m-%d") in self.HOLIDAYS):
            stop_working_time = self.received_time + timedelta(days=8-stop_working_time.isoweekday())
            stop_working_time = stop_working_time.replace(
                hour = self.open_business_time.hour + int(remaining_time.seconds/3600)
            )
            if (stop_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (stop_working_time.strftime("%m-%d") in self.HOLIDAYS):
                stop_working_time += timedelta(days=1)
        
        while (stop_working_time.time() >= self.close_business_time) \
            or (stop_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (stop_working_time.strftime("%m-%d") in self.HOLIDAYS):
            stop_working_time += timedelta(days=1)
            stop_working_time = stop_working_time.replace(
                hour = self.open_business_time.hour + int(remaining_time.seconds/3600)
            )
            if (stop_working_time.strftime("%Y-%m-%d") in self.HOLIDAYS) \
            or (stop_working_time.strftime("%m-%d") in self.HOLIDAYS):
                stop_working_time += timedelta(days=1)
        return stop_working_time
    def calculate_reply_time(self):
        start_working_time = self.calculate_start_working_time()
        stop_working_time = self.calculate_stop_working_time(start_working_time)
        print("Received time: ", start_working_time.strftime("%Y-%m-%d %H:%M:%S"))
        print("Reply time: ", stop_working_time.strftime("%Y-%m-%d %H:%M:%S"))
        return stop_working_time


if __name__=="__main__":
    biz_open_time = time(9, 0, 0)
    biz_close_time = time(18, 0, 0)
    reply_time = ReplyTime(
        received_time=datetime(2022, 4, 15, 17, 00, 00),
        duration_in_hour=4,
        open_business_time=biz_open_time,
        close_business_time=biz_close_time
    )
    reply_time = reply_time.calculate_reply_time()