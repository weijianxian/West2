from Basic import Pokemon, PokemonType
from utils import *


class WaterType(PokemonType):
    """
    水属性宝可梦类型类
    """

    name = "[cyan]水[/]"
    strong_against = []
    weak_against = []

    def onRoundBegin(self, pokemon: Pokemon):
        """
        宝可梦战斗回合开始
        """
        print(f"{pokemon.name} 使用了水属性被动")
        pokemon.hp += pokemon.hp * 0.1


class GrassType(PokemonType):
    """
    草属性宝可梦类型类
    """

    name = "[green]草[/]"
    strong_against = []
    weak_against = []


class FireType(PokemonType):
    """
    火属性宝可梦类型类
    """

    name = "[red]火[/]"
    strong_against = []
    weak_against = []


class ElectricType(PokemonType):
    """
    电属性宝可梦类型类
    """

    name = "[yellow]电[/]"
    strong_against = []
    weak_against = []


WaterType.strong_against = [FireType]
WaterType.weak_against = [ElectricType]

GrassType.strong_against = [WaterType]
GrassType.weak_against = [FireType]

FireType.strong_against = [GrassType]
FireType.weak_against = [WaterType]

ElectricType.strong_against = [WaterType]
ElectricType.weak_against = [GrassType]
