'''
6. Delta time calculator - write a script that calculates
time difference in days between current date and
custom date in the future.
'''

from datetime import datetime
import calendar


def count_days(date):
    date_now = datetime.utcnow()
    if date < date_now:
        print("Date should be from future")
        return
    days = 0
    if date_now.year == date.year:
        if date_now.month == date.month:
            days = date.day - date_now.day
            return days
        else:
            # add left days from current month
            day_in_month = calendar.monthrange(
                date_now.year, date_now.month)[1]
            days = day_in_month - date_now.day
            # add days from next months
            current_month = date_now.month + 1
            day_in_month = calendar.monthrange(date_now.year, current_month)[1]
            while current_month < date.month:
                days += day_in_month
                current_month += 1
                day_in_month = calendar.monthrange(
                    date_now.year, current_month)[1]
            # add days in last month
            days += date.day
    else:
        # year is changing
        # add left days from current month
        day_in_month = calendar.monthrange(date_now.year, date_now.month)[1]
        days = day_in_month - date_now.day
        # add days from next months
        current_month = date_now.month + 1
        while current_month <= 12:
            days += calendar.monthrange(date_now.year, current_month)[1]
            current_month += 1
        # add years 366 leap 365 esle
        curren_year = date_now.year + 1
        while curren_year < date.year:
            if calendar.isleap(curren_year):
                days += 366
            else:
                days += 365
            curren_year += 1
        # add days form months from last year
        current_month = 1
        while current_month < date.month:
            days += calendar.monthrange(date.year, current_month)[1]
            current_month += 1
        # add days from last month
        days += date.day
    return days


if __name__ == "__main__":
    print("")
    future_date = datetime(2050, 1, 1)
    print("From today till ", '{:%Y %B %d}'.format(future_date),
          "there is ", count_days(future_date), "day(s) left.")
    future_date = datetime(2018, 12, 18)
    print("From today till ", '{:%Y %B %d}'.format(future_date),
          "there is ", count_days(future_date), "day(s) left.")
    future_date = datetime(2018, 8, 1)
    print("From today till ", '{:%Y %B %d}'.format(future_date),
          "there is ", count_days(future_date), "day(s) left.")
    future_date = datetime(2019, 4, 29)
    print("From today till ", '{:%Y %B %d}'.format(future_date),
          "there is ", count_days(future_date), "day(s) left.")
    future_date = datetime(2019, 5, 30)
    print("From today till ", '{:%Y %B %d}'.format(future_date),
          "there is ", count_days(future_date), "day(s) left.")
    future_date = datetime(2018, 12, 31)
    print("From today till ", '{:%Y %B %d}'.format(future_date),
          "there is ", count_days(future_date), "day(s) left.")
