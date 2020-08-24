# 1061 Event Time
from datetime import datetime, timedelta

starting_day = int(input().replace("Dia ", ""))
start_of_event = input().replace(" ", "")
starting_hour, starting_minute, starting_second = map(
    int, start_of_event.split(":"))
ending_day = int(input().replace("Dia ", ""))
end_of_event = input().replace(" ", "")
ending_hour, ending_minute, ending_second = map(int, end_of_event.split(":"))

start = datetime(2020, 1, starting_day, starting_hour,
                 starting_minute, starting_second)
end = datetime(2020, 1, ending_day, ending_hour, ending_minute, ending_second)
# using datetime.datetime.total_seconds() and datetime.timedelta(seconds={}) to store the time in a timedelta class
time_in_seconds = timedelta(seconds=int((end - start).total_seconds()))


def get_time():
    global time_in_seconds
    d = datetime(1, 1, 1) + time_in_seconds

    print("{} dia(s)".format(d.day-1))
    print("{} hora(s)".format(d.hour))
    print("{} minuto(s)".format(d.minute))
    print("{} segundo(s)".format(d.second))


get_time()
