import random as rd

from utils import *


class Player:

    def __init__(
        self,
        name: str,
        fightPokemon: "Pokemon",
        pokemons: list["Pokemon"],
        target: "Player" = None,
    ):
        self.name: str = name  # 玩家名称
        self.onFightPokemon: Pokemon = fightPokemon  # 当前出战的宝可梦
        self.pokemons: list[Pokemon] = pokemons  # 拥有的宝可梦
        self.target: "Player" = target  # 对手

    def onRoundStart(self):
        """
        回合开始
        """
        self.onFightPokemon.onRoundBegin()

    def onRoundEnd(self):
        """
        回合结束
        """
        self.onFightPokemon.onRoundEnd()

    def switchPokemon(self, pokemon: "Pokemon"):
        """
        切换宝可梦
        """
        if pokemon not in self.pokemons:
            raise ValueError("宝可梦不在列表中")

        self.onFightPokemon = pokemon

    def getOnFightPokemon(self):
        return self.onFightPokemon


class Pokemon:
    """
    基础宝可梦类

    name: 宝可梦名称
    hp: 宝可梦生命值
    type: 宝可梦类型
    attack: 宝可梦攻击力
    defense: 宝可梦防御力
    evasion: 宝可梦闪避率 0-100 之间,
    status: 宝可梦状态
    """

    name: str = ""
    hp: int = 0
    type: "PokemonType" = None
    attack: int = 0
    defense: int = 0
    evasion: int = 0
    status_list: list["Status"] = []
    skill_list: list["Skill"] = []

    def __init__(self):
        self.skill_list = [skill() for skill in self.skill_list]

    def __str__(self):
        return f"{self.name}({self.type.name})"

    def onRoundBegin(self):
        """
        宝可梦战斗回合开始,处理状态,计算闪避率等
        """
        pass

    def fight(self, user: "Pokemon", target: "Pokemon", skill: "Skill"):
        """
        宝可梦战斗
        """
        # 闪避判断
        if rd.randint(0, 100) < target.evasion:
            print(f"{target.name} [red]闪避了[/] {user.name} 的攻击")
            return

        # 破防判断
        elif self.attack < target.defense:
            print(f"{target.name} 的[red]防御力过高[/]，{user.name} 的攻击对其无效")
            return

        # 攻击
        skill.use(
            user,
            target,
        )

    def onRoundEnd(self):
        """
        宝可梦战斗回合结束
        """
        pass


class PokemonType:
    """
    基础宝可梦类型类

    name: 宝可梦类型名称
    strong_against: 强势对手
    weak_against: 弱势对手
    """

    name: str = ""

    strong_against: list["PokemonType"] = []
    weak_against: list["PokemonType"] = []

    def on_begin(self):
        pass


class Skill:
    name = "基础技能"
    description = "技能描述"

    def use(self, user: Pokemon, target: Pokemon):
        print("[red]未实现[/]")
        pass


class Status:
    """
    Represents a basic status in the Pokemon game.
    Attributes:
        name (str): 名称
        priority(int): 越大越先执行,0为最后执行,同优先级按照加入顺序
        continue_round (int): 持续回合数,-1为永久,0为即时
    """

    name = "BasicStatus"
    priority = 0
    continue_round = 0

    def on_apply(self, pokemon: Pokemon):
        """
        状态生效
        :param pokemon: 宝可梦(自身)
        """
        pass
