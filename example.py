# -*- coding: utf-8 -*-

from covid19umbria import Covid19Umbria

if __name__ == "__main__":
    # fetch data
    covid19 = Covid19Umbria()

    current_active = covid19.get_current_active_cases()
    new_active = covid19.get_new_active_cases()
    deaths = covid19.get_total_deaths()
    recovered = covid19.get_total_recovered()

    print(f"Current active: {current_active}, new active: {new_active}, deaths: {deaths}, recovered: {recovered}")
