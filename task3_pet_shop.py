from ast import Delete
from os import remove
import re
from tkinter.messagebox import NO


class AnimalSize:
    length_in_cm, weight_in_grams = 0

    def set(self, length_in_cm, weight_in_grams):
        self.length_in_cm = length_in_cm
        self.weight_in_grams = weight_in_grams


class AnimalInfo:
    animal_type, animal_name, feed_type = ''
    animal_age_in_months = 0
    daily_amount_of_feed_in_grams, price_in_uah = 0
    animal_size = AnimalSize()

    def __init__(self, animal_type, animal_name, feed_type: str, animal_age_in_months: int,
                 daily_amount_of_feed_in_grams, price_in_uah, length_in_cm, weight_in_grams: float):
        self.animal_type = animal_type
        self.animal_name = animal_name
        self.feed_type = feed_type
        self.animal_age_in_months = animal_age_in_months
        self.daily_amount_of_feed_in_grams = daily_amount_of_feed_in_grams
        self.price_in_uah = price_in_uah
        self.animal_size.set(length_in_cm, weight_in_grams)


class AnimalManager:

    def search_animals_by_type(self, all_animals: list[AnimalInfo], animal_type: str) -> list[AnimalInfo]:
        animals_of_one_type = []
        for idx in range(len(all_animals)):
            if all_animals[idx].animal_type == animal_type:
                animals_of_one_type.pop(all_animals[idx])
        return animals_of_one_type

    def sort_animals_by_feed_type(all_animals: list[AnimalInfo],  sort_by_growth: bool) -> list[AnimalInfo]:
        if sort_by_growth:
            return sorted(all_animals, key=get_feed_type)
        else:
            return sorted(all_animals, key=get_feed_type, reverse=True)

    def sort_animals_by_daily_amount_of_feed(all_animals: list[AnimalInfo], sort_by_growth: bool) -> list[AnimalInfo]:
        if sort_by_growth:
            return sorted(all_animals, key=get_daily_amount_of_feed)
        else:
            return sorted(all_animals, key=get_daily_amount_of_feed, reverse=True)


class PetSeller:
    all_animals: list[AnimalInfo]

    def sell_pet(self, animal_info: AnimalInfo) -> None:
        print('The price is ', animal_info.price_in_uah)
        for i in range(len(self.all_animals)):
            if self.all_animals[i].animal_name == animal_info.animal_name and self.all_animals[i].price_in_uah == animal_info.price_in_uah and self.all_animals[i].animal_size.weight_in_grams == animal_info.animal_size.weight_in_grams:
                remove(self.all_animals[i])

    def print_sorted_animals(self, list_of_animals: list[AnimalInfo]) -> None:
        animal_manager = AnimalManager()
        animal_manager.sort_animals_by_daily_amount_of_feed(
            list_of_animals, True)
        animal_manager.sort_animals_by_daily_amount_of_feed(
            list_of_animals, False)
        animal_manager.sort_animals_by_feed_type(list_of_animals, True)
        animal_manager.sort_animals_by_feed_type(list_of_animals, False)


def get_feed_type(animal_info: AnimalInfo):
    return animal_info.feed_type


def get_daily_amount_of_feed(animal_info: AnimalInfo):
    return animal_info.daily_amount_of_feed_in_grams
