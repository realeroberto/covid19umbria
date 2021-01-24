# -*- coding: utf-8 -*-

import datetime
from covid19umbria import Covid19Umbria

numdays = 30 # last 30 days

if __name__ == "__main__":
    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]

    # fetch data
    covid19 = Covid19Umbria()

    for date in date_list:
        current_active = covid19.get_current_active_cases(date)
        total_confirmed = covid19.get_total_confirmed_cases(date)
        deaths = covid19.get_total_deaths(date)
        recovered = covid19.get_total_recovered(date)

        print(f"Date: {date.strftime('%Y-%m-%d')}, current active: {current_active}, total confirmed: {total_confirmed}, deaths: {deaths}, recovered: {recovered}")
