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
        new_active = covid19.get_new_active_cases(date)
        deaths = covid19.get_total_deaths(date)
        recovered = covid19.get_total_recovered(date)

        print(f"Date: {date.strftime('%Y-%m-%d')}, current active: {current_active}, new active: {new_active}, deaths: {deaths}, recovered: {recovered}")
