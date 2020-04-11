from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any

from postman_covid19_sdk.utils.enums import CategoryType, StatusType

if TYPE_CHECKING:
    from enum import Enum
    from pandas import DataFrame
    from datetime import datetime

__all__ = [
    "BaseClient"
]


class BaseClient(ABC):
    _DEFAULT_URL = "https://api.covid19api.com/"
    _SUMMARY_URL = "https://api.covid19api.com/summary"
    _COUNTRIES_URL = "https://api.covid19api.com/countries"
    _DAY_ONE_URL = "https://api.covid19api.com/dayone/country/{country}/status/{status}"
    _DAY_ONE_LIVE_URL = "https://api.covid19api.com/dayone/country/{country}/status/{status}/live"
    _DAY_ONE_TOTAL_URL = "https://api.covid19api.com/total/dayone/country/{country}/status/{status}"
    _BY_COUNTRY_URL = "https://api.covid19api.com/country/{country}/status/{status}"
    _BY_COUNTRY_LIVE_URL = "https://api.covid19api.com/country/{country}/status/{status}/live"
    _BY_COUNTRY_TOTAL_URL = "https://api.covid19api.com/total/country/{country}/status/{status}"
    _LIVE_BY_COUNTRY_AND_STATUS_URL = "https://api.covid19api.com/live/country/{country}/status/{status}"
    _LIVE_BY_COUNTRY_AND_STATUS_AFTER_DATE_URL = ("https://api.covid19api.com/live/country/{country}/"
                                                  "status/{status}/date/{date}")
    _ALL_DATA = "https://api.covid19api.com/all"
    _STATS = "https://api.covid19api.com/stats"

    CategoryType: 'CategoryType' = CategoryType
    StatusType: 'StatusType' = StatusType
    Country: 'Enum' = None

    @abstractmethod
    def get_default(self) -> 'DataFrame':
        pass

    @abstractmethod
    def get_summary(self) -> 'DataFrame':
        pass

    @abstractmethod
    def get_countries(self) -> 'DataFrame':
        pass

    @abstractmethod
    def get_day_one(self, country: 'Country', category: 'CategoryType', status: 'StatusType') -> 'DataFrame':
        pass

    @abstractmethod
    def get_by_country(self, country: 'Country', category: 'CategoryType', status: 'StatusType') -> 'DataFrame':
        pass

    @abstractmethod
    def stream_live(self, country: 'Country', status: 'StatusType', date: 'datetime' = None) -> 'DataFrame':
        pass

    @abstractmethod
    def get_all_data(self) -> 'DataFrame':
        pass

    @abstractmethod
    def get_stats(self) -> 'DataFrame':
        pass
