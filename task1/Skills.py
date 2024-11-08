import random as rd

from Basic import Pokemon, Skill
from Status import *
from utils import *


class CommonFigth(Skill):
    name = "[yellow]普通攻击[/]"
    description = "对敌人造成 1 倍攻击力的伤害"

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了普通攻击")
        target.hp -= user.attack
        print(f"{target.name} 受到了 {user.attack} 点伤害")


class Thunderbolt(Skill):
    name = "[yellow]十万伏特[/]"
    description = "对敌人造成 1.4 倍攻击力的电属性伤害，并有 10% 概率使敌人麻痹"

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了十万伏特")
        if rd.randint(0, 100) < 100:
            print(f"{target.name} 被麻痹了")
            target.status_list.append(ParalysisStatus())


class QuickAttack(Skill):
    name = "[yellow]电光一闪[/]"
    description = (
        "对敌人造成 1.0 倍攻击力的快速攻击（有几率触发第二次攻击），10% 概率触发第二次"
    )

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了电光一闪")
        target.hp -= user.attack
        print(f"{target.name} 受到了 {user.attack} 点伤害")
        if rd.randint(0, 100) < 10:
            print(f"[red]技能判定生效[/]，{user.name} 触发了第二次攻击")
            target.hp -= user.attack
            print(f"{target.name} 受到了 {user.attack} 点伤害")


class SeedBomb(Skill):
    name = "[yellow]种子炸弹[/]"
    description = (
        "有50%概率命中，对敌人造成 1.4 倍攻击力的草属性伤害，并有 15% 概率使敌人中毒"
    )

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了种子炸弹")
        if rd.randint(0, 100) < 50:
            print(f"{target.name} 被种子炸弹击中")
            target.hp -= user.attack
            print(f"{target.name} 受到了 {user.attack} 点伤害")
            if rd.randint(0, 100) < 15:
                print(f"{target.name} 中毒了")
                target.status_list.append(PoisonStatus())


class ParasiticSeeds(Skill):
    name = "[yellow]寄生种子[/]"
    description = "向对手播种，每回合吸取对手10%的最大生命值并恢复自己, 效果持续3回合"

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了寄生种子")
        target.status_list.append(LeechStatus(leeched=target, leecher=user, rate=0.1))


class AquaJet(Skill):
    name = "[yellow]水枪[/]"
    description = "杰尼龟喷射出一股强力的水流，对敌方造成 140% 水属性伤害"

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了水枪")
        target.hp -= user.attack * 1.4
        print(f"{target.name} 受到了 {user.attack * 1.4} 点伤害")


# WIP 暂未实现护盾功能
# class Shield(Skill):
#     name = "[yellow]护盾[/]"
#     description = "杰尼龟使用水流形成保护盾，减少下一回合受到的伤害50%"

#     def use(self, user: Pokemon, target: Pokemon):
#         print(f"{user.name} 使用了护盾")
#         target.status_list.append(ShieldStatus())


class Ember(Skill):
    name = "[yellow]火花[/]"
    description = "小火龙发射出一团小火焰，对敌人造成 100% 火属性伤害，并有10%的几率使目标陷入“烧伤”状态"

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了火花")
        target.hp -= user.attack
        print(f"{target.name} 受到了 {user.attack} 点伤害")
        if rd.randint(0, 100) < 10:
            print(f"{target.name} 被烧伤了")
            target.status_list.append(BurnStatus())


class FlameCharge(Skill):
    name = "[yellow]蓄能爆炎[/]"
    description = "小火龙召唤出强大的火焰，对敌人造成 300% 火属性伤害，并有80%的几率使敌人陷入“烧伤”状态，这个技能需要1个回合的蓄力，并且在面对改技能时敌法闪避率增加 20%"

    def use(self, user: Pokemon, target: Pokemon):
        print(f"{user.name} 使用了蓄能爆炎")
        target.hp -= user.attack * 3
        print(f"{target.name} 受到了 {user.attack * 3} 点伤害")
        if rd.randint(0, 100) < 80:
            print(f"{target.name} 被烧伤了")
            target.status_list.append(BurnStatus())
