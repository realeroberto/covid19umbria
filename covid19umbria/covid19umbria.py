# -*- coding: utf-8 -*-

""" Covid-19 statistics for Regione Umbria, based on the public API

    Cf. https://github.com/Regione-Umbria/coronavirus
"""

import requests
from datetime import date, timedelta

URL = "https://api.regione.umbria.it:443/covid19/1.0.0/dati"
LIMIT = 100000


class Covid19Umbria(object):

    def __init__(self):
        self.__limit = LIMIT
        self.__cache = dict()
        
    def __yesterday(self):
        yesterday = date.today() - timedelta(days=1)
        return yesterday

    def __get_date(self, date=None):
        if date is None:
            date = self.__yesterday()
        return date

    def refresh(self, date=None):
        if date is None:
            for k in self.__cache.items():
                del k
        else:
            try:
                del self.__cache[date]
            except KeyError:
                pass

    def get_data(self, date=None) -> list:
        """ Fetch all data
        """

        date = self.__get_date(date)

        try:
            return self.__cache[date]
        except KeyError:
            pass

        params = dict(
            data=date.strftime('%Y-%m-%d'),
            offset=1,
            limit=self.__limit,
        )

        response = requests.get(URL, params=params).json()

        try:
            self.__cache[date] = response["results"]
            return response["results"]
        except KeyError:
            raise Exception(response)

    def get_raw_data(self, date=None) -> list:
        return self.get_data(date)

    def get_date(self, date=None) -> str:
        return self.__get_date(date)

    def get_current_active_cases(self, date=None) -> int:
        """ Current number of active cases
        """
        return sum(d['attualmente_positivi'] for d in self.get_data(date))

    def get_new_active_cases(self, date=None) -> int:
        """ Number of confirmed cases
        """
        return sum(d['casi_positivi'] for d in self.get_data(date))

    def get_total_deaths(self, date=None) -> int:
        """ Number of deaths
        """
        return sum(d['deceduti'] for d in self.get_data(date))

    def get_total_recovered(self, date=None) -> int:
        """ Number of recovered cases
        """
        return sum(d['guariti'] for d in self.get_data(date))
