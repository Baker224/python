duration = int(input('duration = '))
day = duration // (60 * 60 * 24)
hour = (duration // (60 * 60)) - (day * 24)
minute = (duration // 60) - (hour * 60) - (day * 24 * 60)
second = duration - (minute * 60) - (hour * 60 * 60) - (day * 60 * 60 * 24)
if minute > 0:
    if hour > 0:
        if day > 0:
            print(day, 'дн', hour, 'час', minute, 'мин', second, 'сек')
        else:
            print(hour, 'час', minute, 'мин', second, 'сек')
    else:
        print(minute, 'мин', second, 'сек')
else:
    print(duration, 'сек')