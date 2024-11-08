from Basic import Pokemon
from PokemonType import ElectricType, FireType, GrassType, WaterType
from Skills import *


class Pikachu(Pokemon):
    """
    皮卡丘宝可梦类
    """

    name = "[yellow]皮卡丘[/]"
    hp = 80
    type = ElectricType
    attack = 35
    defense = 5
    evasion = 30
    skill_list = [CommonFigth, Thunderbolt, QuickAttack]


class Bulbasaur(Pokemon):
    """
    妙蛙种子宝可梦类
    """

    name = "[green]妙蛙种子[/]"
    hp = 100
    type = GrassType
    attack = 35
    defense = 10
    evasion = 10
    skill_list = [CommonFigth, SeedBomb, ParasiticSeeds]


class Squirtle(Pokemon):
    """
    杰尼龟宝可梦类
    """

    name = "[blue]杰尼龟[/]"
    hp = 80
    type = WaterType
    attack = 25
    defense = 20
    evasion = 20
    skill_list = [CommonFigth, AquaJet]


class Charmander(Pokemon):
    """
    小火龙宝可梦类
    """

    name = "[red]小火龙[/]"
    hp = 80
    type = FireType
    attack = 35
    defense = 15
    evasion = 10
    skill_list = [CommonFigth, Ember, FlameCharge]


PokemonList: list[Pokemon] = [Pikachu, Bulbasaur, Squirtle, Charmander]
