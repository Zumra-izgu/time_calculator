def add_time(start_time, duration):
    finish_time = " "
    the_day_after = " "
    hours= []
    minutes= []


    hours = start_time.split(":")[0]

    minutes = start_time.split(":")[1]

    second_hour = duration.split (":")[0]

    second_minute = duration.split(":")[1]

    hours = int(hours)
    minutes= int(minutes)
    second_minute = int(second_minute)
    second_hour = int(second_hour)
    hours += second_hour
    minutes += second_minute
    print(hours)
    print(minutes)

    if (minutes > 60):
        hours += int (minutes) // 60
        minutes= int(minutes) % 60

    if (hours > 24):
        the_day_after = int(hours) // 24
        hours = int(hours) % 24

    hours= str(hours)
    minutes= str(minutes)
    finish_time = ":". join ((hours, minutes))
    the_day_after = str(the_day_after)

    if int(finish_time.split(":")[0]) >= 12:
        print("{} PM, {} days later". format (finish_time, the_day_after))

    if int(finish_time.split(":")[0]) < 12:
        print("{} AM, {} days later".format(finish_time, the_day_after))




add_time("24:50" , "1:45")
