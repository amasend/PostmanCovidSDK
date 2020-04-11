import requests
from typing import Dict

from .base_client import BaseClient

from pandas import DataFrame
from pandas import to_datetime
from datetime import datetime

__all__ = [
    "APIClient"
]


class APIClient(BaseClient):
    Countries = type('Countries', (),
                     {entry['Country'].strip().upper().replace(' ', '_').replace(',', '_'): entry['Slug'] for entry in
                      requests.request("GET", url=BaseClient._COUNTRIES_URL).json() if entry['Country'] != ''
                      }
                     )

    def __init__(self):
        pass

    def get_default(self) -> dict:
        """
        List all the current routes available with detail on each.

        Returns
        -------
        pandas.DataFrame
        """

        payload = {}
        headers = {}

        response = requests.request("GET", url=BaseClient._DEFAULT_URL, headers=headers, data=payload)
        return response.json()

    def get_summary(self) -> Dict[str, 'DataFrame']:
        """
        A summary of new and total cases per country updated daily.

        Returns
        -------
        pandas.DataFrame
        """

        payload = {}
        headers = {}

        response = requests.request("GET", url=BaseClient._SUMMARY_URL, headers=headers, data=payload)

        return {'Global': DataFrame(response.json()['Global'], index=[0]),
                'Countries': DataFrame(response.json()['Countries']).set_index('Country')}

    def get_countries(self) -> 'DataFrame':
        """
        Returns all the available countries and provinces, as well as the country slug for per country requests.

        Returns
        -------
        pandas.DataFrame
        """

        payload = {}
        headers = {}

        response = requests.request("GET", url=BaseClient._COUNTRIES_URL, headers=headers, data=payload)
        return DataFrame(response.json()).set_index('Country')

    def get_day_one(self,
                    country: 'APIClient.Country',
                    category: 'APIClient.CategoryType' = BaseClient.CategoryType.DEFAULT,
                    status: 'APIClient.StatusType' = BaseClient.StatusType.CONFIRMED) -> 'DataFrame':
        """
        Returns all cases by case type for a country from the first recorded case.

        Parameters
        ----------
        country: APIClient.Country, required
            Specific country name.

        category: APIClient.CategoryType, optional
            One of [DEFAULT, LIVE, TOTAL]

        status: APIClient.StatusType, optional
            One of [CONFIRMED, RECOVERED, DEATHS]

        Returns
        -------
        pandas.DataFrame
        """
        if category == BaseClient.CategoryType.DEFAULT:
            url = BaseClient._DAY_ONE_URL.format(country=country, status=status.value)

        elif category == BaseClient.CategoryType.LIVE:
            url = BaseClient._DAY_ONE_LIVE_URL.format(country=country, status=status.value)

        else:
            url = BaseClient._DAY_ONE_TOTAL_URL.format(country=country, status=status.value)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = self._date_index(response)

        return data

    def get_by_country(self,
                       country: 'APIClient.Country',
                       category: 'APIClient.CategoryType' = BaseClient.CategoryType.DEFAULT,
                       status: 'APIClient.StatusType' = BaseClient.StatusType.CONFIRMED) -> 'DataFrame':
        """
        Returns all cases by case type for a country.

        Parameters
        ----------
        country: APIClient.Country, required
            Specific country name.

        category: APIClient.CategoryType, optional
            One of [DEFAULT, LIVE, TOTAL]

        status: APIClient.StatusType, optional
            One of [CONFIRMED, RECOVERED, DEATHS]

        Returns
        -------
        pandas.DataFrame
        """

        if category == BaseClient.CategoryType.DEFAULT:
            url = BaseClient._BY_COUNTRY_URL.format(country=country, status=status.value)

        elif category == BaseClient.CategoryType.LIVE:
            url = BaseClient._BY_COUNTRY_LIVE_URL.format(country=country, status=status.value)

        else:
            url = BaseClient._BY_COUNTRY_TOTAL_URL.format(country=country, status=status.value)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = self._date_index(response)

        return data

    def stream_live(self,
                    country: 'APIClient.Country',
                    status: 'APIClient.StatusType' = BaseClient.StatusType.CONFIRMED,
                    date: 'datetime' = None) -> dict:
        """
        Returns all live cases by case type for a country. These records are pulled every 10 minutes and are ungrouped.

        Parameters
        ----------
        country: APIClient.Country, required
            Specific country name.

        status: APIClient.StatusType, optional
            One of [CONFIRMED, RECOVERED, DEATHS]

        date: datetime, optional
            If None, current date will be used.

        Returns
        -------
        pandas.DataFrame
        """
        if date is None:
            url = BaseClient._LIVE_BY_COUNTRY_AND_STATUS_URL.format(country=country, status=status.value)

        else:
            url = BaseClient._LIVE_BY_COUNTRY_AND_STATUS_AFTER_DATE_URL.format(country=country, status=status.value,
                                                                               date=date)

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        data = self._date_index(response)

        return data

    def get_all_data(self) -> dict:
        """
        Returns all daily data. This call results in 10MB of data being returned and should be used infrequently.

        Returns
        -------
        pandas.DataFrame
        """

        payload = {}
        headers = {}

        response = requests.request("GET", BaseClient._ALL_DATA, headers=headers, data=payload)

        return response.json()

    def get_stats(self) -> dict:
        """
        Statistics of Postman API endpoints.

        Returns
        -------
        pandas.DataFrame
        """

        payload = {}
        headers = {
            'Origin': 'http://localhost'
        }

        response = requests.request("GET", BaseClient._STATS, headers=headers, data=payload)

        return response.json()

    @staticmethod
    def _date_index(response) -> 'DataFrame':
        """Set 'Date' as an index and convert it to a datetime representation."""
        data = DataFrame(response.json())
        data["Date"] = to_datetime(data["Date"], format="%Y-%m-%d %H:%M")
        data.index = data["Date"]
        data.drop("Date", 1, inplace=True)

        return data
