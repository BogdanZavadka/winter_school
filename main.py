import datetime
from datetime import date
from typing import List, Union

'''class Fish:

    def __init__(self) -> None:
        self.name = "oseledets"
        self.price_in_uah_per_kilo = 11.2
        self.catch_date = datetime("21/01/2022")
        self.origin = "Norway"
        self.body_only = True
        self.weight = 100'''


class FishShop:
    fish_name = ''
    weight = 0
    price_in_uah_per_kilo = 0
    catch_date = date(2022, 1, 1)

    expiration_date = date(2022, 2, 1)

    def add_fish(self, fish_name: str, weight, price_in_uah_per_kilo: float, catch_date: datetime) -> None:
        self.fish_name = fish_name
        self.weight = weight
        self.price_in_uah_per_kilo = price_in_uah_per_kilo
        self.catch_date = catch_date

    #def get_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
    #   pass

    def sell_fish(self, fish_name: str, weight: float) -> float:
        if fish_name == self.fish_name:
            return self.price_in_uah_per_kilo * weight

    def cast_out_old_fish(self) -> str:
        list1 = List
        if self.catch_date >= self.expiration_date:
            return self.fish_name


class Seller:
    def sort_fish_on_counter(self, fish_name) -> None:
        pass

    def show_product_information(self, fish_name, price_in_uah_per_kilo, catch_date, origin) -> List:
        pass

    def sell_product(self, fish_name, weight) -> float:
        pass


class Buyer:
    def check_freshness_of_product(self, catch_date) -> bool:
        pass

    def buy_fish(self, price_in_uah_per_kilo, weight) -> float:
        pass

