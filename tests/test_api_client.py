import unittest

from postman_covid19_sdk.client import APIClient
from postman_covid19_sdk.utils.enums import StatusType, CategoryType


class TestAPIClient(unittest.TestCase):
    client: 'APIClient' = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.client = APIClient()

    def test_01_get_countries(self):
        countries = self.client.get_countries()

        print(countries)

    def test_02_get_default(self):
        results = self.client.get_default()

        print(results)

    def test_03_get_summary(self):
        results = self.client.get_summary()

        print(results)

    def test_04A_get_day_one_confirmed(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.CONFIRMED)

        print(results)

    def test_04B_get_day_one_recovered(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.RECOVERED)

        print(results)

    def test_04C_get_day_one_deaths(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.DEATHS)

        print(results)

    def test_04D_get_day_one_confirmed_live(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.CONFIRMED,
                                          category=CategoryType.LIVE)

        print(results)

    def test_04E_get_day_one_recovered_live(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.RECOVERED,
                                          category=CategoryType.LIVE)

        print(results)

    def test_04F_get_day_one_deaths_live(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.DEATHS,
                                          category=CategoryType.LIVE)

        print(results)

    def test_04G_get_day_one_confirmed_total(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.CONFIRMED,
                                          category=CategoryType.TOTAL)

        print(results)

    def test_04H_get_day_one_recovered_total(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.RECOVERED,
                                          category=CategoryType.TOTAL)

        print(results)

    def test_04I_get_day_one_deaths_total(self):
        results = self.client.get_day_one(country=self.client.Countries.POLAND, status=StatusType.DEATHS,
                                          category=CategoryType.TOTAL)

        print(results)

    def test_05A_get_by_country_confirmed(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.CONFIRMED)

        print(results)

    def test_05B_get_by_country_recovered(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.RECOVERED)

        print(results)

    def test_05C_get_by_country_deaths(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.DEATHS)

        print(results)

    def test_05D_get_by_country_confirmed_live(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.CONFIRMED,
                                             category=CategoryType.LIVE)

        print(results)

    def test_05E_get_by_country_recovered_live(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.RECOVERED,
                                             category=CategoryType.LIVE)

        print(results)

    def test_05F_get_by_country_deaths_live(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.DEATHS,
                                             category=CategoryType.LIVE)

        print(results)

    def test_05G_get_by_country_confirmed_total(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.CONFIRMED,
                                             category=CategoryType.TOTAL)

        print(results)

    def test_05H_get_by_country_recovered_total(self):
        results = self.client.get_by_country(country=self.client.Countries.POLAND, status=StatusType.RECOVERED,
                                             category=CategoryType.TOTAL)

        print(results)

    def test_06_stream_live(self):
        results = self.client.stream_live(country=self.client.Countries.POLAND)

        print(results)

    def test_07_get_all_data(self):
        results = self.client.get_all_data()

        print(results)

    def test_08_get_stats(self):
        results = self.client.get_stats()

        print(results)


if __name__ == '__main__':
    unittest.main()
