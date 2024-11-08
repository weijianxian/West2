from Basic import Player, Pokemon
from Pokemon import *
from utils import *


class Player(Player):

    def __str__(self) -> str:
        return self.name

    def onRoundStart(self):
        """
        回合开始
        """

        # 检查状态
        for status in self.onFightPokemon.status_list:
            if status.continue_round == 0:
                self.onFightPokemon.status_list.remove(status)

            is_skip_round = status.on_apply(self.onFightPokemon)
            if is_skip_round:
                return

        # 选择技能
        for i, skill in enumerate(self.onFightPokemon.skill_list):
            print(f"[{i}] {skill.name}: {skill.description}")

        index = int(
            question(
                "请选择技能: ",
                [str(i) for i in range(len(self.onFightPokemon.skill_list))],
            )
        )
        # 使用技能
        self.onFightPokemon.fight(
            self.onFightPokemon,
            self.target.onFightPokemon,
            self.onFightPokemon.skill_list[index],
        )

    def onRoundEnd(self):
        """
        回合结束
        """
        self.onFightPokemon.onRoundEnd()


class AI(Player):

    def onRoundStart(self):
        """
        回合开始
        """
        self.onFightPokemon.fight(
            self.onFightPokemon,
            self.target.onFightPokemon,
            self.onFightPokemon.skill_list[0],
        )

    def onRoundEnd(self):
        """
        回合结束
        """
        self.onFightPokemon.onRoundEnd()

    def switchPokemon(self, pokemon: Pokemon):
        """
        切换宝可梦
        """
        if pokemon not in self.pokemons:
            raise ValueError("宝可梦不在列表中")

        self.onFightPokemon = pokemon


class RemotePlayer:
    # TODO: Implement this class
    # 远程玩家
    pass
