from Basic import Pokemon, Status
from utils import *


class PoisonStatus(Status):
    name = "中毒"
    priority = 1
    continue_round = 3

    def on_apply(self, pokemon: Pokemon):
        print(f"{pokemon.name} 中毒了")
        pokemon.hp -= int(pokemon.hp * 0.1)

        self.continue_round -= 1


class ParalysisStatus(Status):
    name = "麻痹"
    priority = 1
    continue_round = 1

    def on_apply(self, pokemon: Pokemon):
        print(f"{pokemon.name} 麻痹了")
        self.continue_round -= 1


class LeechStatus(Status):
    name = "吸血"
    priority = 1
    continue_round = 3

    def __init__(self, leeched: "Pokemon", leecher: "Pokemon", rate: int = 0.1):
        """
        :param leeched: 被吸血的宝可梦
        :param leecher: 吸血的宝可梦
        :param rate: 吸血比例
        """

        self.leeched = leeched
        self.leecher = leecher
        self.rate = rate

    def on_apply(self, pokemon: Pokemon):
        print(f"{pokemon.name} 被吸血了")
        self.leecher.hp += int(self.leeched.hp * self.rate)

        self.continue_round -= 1


class BurnStatus(Status):
    name = "灼伤"
    priority = 1
    continue_round = 3

    def on_apply(self, pokemon: Pokemon):
        print(f"{pokemon.name} 灼伤了")
        pokemon.hp -= int(pokemon.hp * 0.1)

        self.continue_round -= 1
