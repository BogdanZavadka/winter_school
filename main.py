import datetime
from datetime import date
from typing import List, Union


class Fish:
    age_in_months = 0
    weight = 0


class FishInfo:
    name = ''
    origin = ''
    catch_date = ''
    due_date = ''


class FishBox:
    fish_info = FishInfo()
    weight = 0
    package_date = ''
    is_fresh = True
    weight = 0
    height = 0
    width = 0
    length = 0


class FishShop:

    frozen_fish_boxes: dict[str: List[FishBox]]
    fresh_fish: dict[str: List[Fish]]

    def add_fish(self, fish_box: FishBox) -> None:
        pass

    def sell_fish(self, name: int, weight: float, is_fresh: bool) -> None:
        pass

    def get_fish_names_sorted_by_price(self) -> List[Union[str, bool, float]]:
        pass

    def get_fresh_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        pass

    def get_frozen_fish_names_sorted_by_price(self) -> List[Union[str, float]]:
        pass


