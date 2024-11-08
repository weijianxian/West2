import random as rd

from Game import Game
from Player import AI, Player
from Pokemon import PokemonList
from utils import *

print(
    """\
[green],-.----.                                                                             [/][red]                        [/] 
[green]\    /  \                    ,-.                       ____                          [/][red]   ,----..              [/] 
[green]|   :    \               ,--/ /|                     ,'  , `.                        [/][red]  /   /   \             [/] 
[green]|   |  .\ :    ,---.   ,--. :/ |                  ,-+-,.' _ |    ,---.         ,---, [/][red] |   :     :     ,---.  [/] 
[green].   :  |: |   '   ,'\  :  : ' /                ,-+-. ;   , ||   '   ,'\    ,-+-. /  |[/][red] .   |  ;. /    '   ,'\ [/] 
[green]|   |   \ :  /   /   | |  '  /       ,---.    ,--.'|'   |  ||  /   /   |  ,--.'|'   |[/][red] .   ; /--`    /   /   |[/] 
[green]|   : .   / .   ; ,. : '  |  :      /     \  |   |  ,', |  |, .   ; ,. : |   |  ,"' |[/][red] ;   | ;  __  .   ; ,. :[/] 
[green];   | |`-'  '   | |: : |  |   \    /    /  | |   | /  | |--'  '   | |: : |   | /  | |[/][red] |   : |.' .' '   | |: :[/] 
[green]|   | ;     '   | .; : '  : |. \  .    ' / | |   : |  | ,     '   | .; : |   | |  | |[/][red] .   | '_.' : '   | .; :[/] 
[green]:   ' |     |   :    | |  | ' \ \ '   ;   /| |   : |  |/      |   :    | |   | |  |/ [/][red] '   ; : \  | |   :    |[/] 
[green]:   : :      \   \  /  '  : |--'  '   |  / | |   | |`-'        \   \  /  |   | |--'  [/][red] '   | '/  .'  \   \  / [/] 
[green]|   | :       `----'   ;  |,'     |   :    | |   ;/             `----'   |   |/      [/][red] |   :    /     `----'  [/] 
[green]`---'.|                '--'        \   \  /  '---'                       '---'       [/][red]  \   \ .'              [/] 
[green]  `---`                             `----'                                           [/][red]   `---`                [/] 
"""
)


def main():
    for index, pokemon in enumerate(PokemonList):
        print(
            f"[green]{index}. {pokemon.name}[/]\t[red]hp: {pokemon.hp}[/]\t[cyan]攻击: {pokemon.attack}[/]\t[yellow]防御: {pokemon.defense}[/]"
        )

    index = int(
        question(
            "[green]请输入你选择的宝可梦编号:[/]",
            [str(i) for i in range(len(PokemonList))],
        )
    )

    user = Player("你", PokemonList[index](), PokemonList)
    ai = AI("电脑", PokemonList[rd.randint(0, 3)](), PokemonList)

    user.target = ai
    ai.target = user

    game = Game(players=[user, ai])

    game.GameLoop()


if __name__ == "__main__":
    main()
