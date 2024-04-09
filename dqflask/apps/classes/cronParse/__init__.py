

def to_cron(value, minutes = None, minute_in_hour = None, hour_in_day = None, minute_in_day = None, hour_in_week = None, minute_in_week = None, day_in_week = None, minute_in_month = None, hour_in_month = None, day_in_month = None):
    number_day_in_week = { 'понедельник' : '1',
                    'вторник': '2',
                    'среда': '3',
                    'четверг': '4',
                    'пятница': '5',
                    'суббота': '6',
                    'воскресенье': '0',
                    }
    if value == 'minutes':
        return '*/' + minutes + ' * * * *'
    elif value == 'hour':
        return minute_in_hour + ' * * * *'
    elif value == 'day':
        return minute_in_day + ' ' + hour_in_day + ' * * *'
    elif value == 'week':
        return minute_in_week + ' ' + hour_in_week + ' * * ' + number_day_in_week[day_in_week]
    elif value == 'month':
        return minute_in_month + ' ' + hour_in_month + ' ' + day_in_month + ' * * '
    elif value == 'none':
        return None


def from_cron(sch):
    value = None
    minutes = None
    minute_in_hour = None
    hour_in_day = None
    minute_in_day = None
    hour_in_week = None
    minute_in_week = None
    day_in_week = None
    hour_in_month = None
    minute_in_month = None
    day_in_month = None
    number_day_in_week = { '1': 'понедельник',
                    '2':'вторник',
                    '3':'среда',
                    '4':'четверг',
                    '5':'пятница',
                    '6':'суббота',
                    '0':'воскресенье',
                  }
    print(sch)
    if sch is not None:
        cron = sch.split()
        if len(cron) == 5:
            if cron[0][0] == '*':
                value = 'minutes'
                minutes = cron[0][2:]
            elif cron[1] == '*':
                value = 'hour'
                minute_in_hour = cron[0]
            elif cron[2] != '*':
                value = 'month'
                minute_in_month = cron[0]
                hour_in_month = cron[1]
                day_in_month = cron[2]
            elif cron[4] == '*':
                value = 'day'
                minute_in_day = cron[0]
                hour_in_day = cron[1]
            elif cron[4] != '*':
                value = 'week'
                minute_in_week = cron[0]
                hour_in_week = cron[1]
                day_in_week = number_day_in_week[cron[4]]
    result = {'value': value,
              'minutes': minutes,
              'minute_in_hour': minute_in_hour,
              'hour_in_day': hour_in_day,
              'minute_in_day': minute_in_day,
              'hour_in_week': hour_in_week,
              'minute_in_week': minute_in_week,
              'day_in_week': day_in_week,
              'hour_in_month': hour_in_month,
              'minute_in_month': minute_in_month,
              'day_in_month': day_in_month
              }
    return result