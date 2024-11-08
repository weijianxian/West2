# PokemonGo

![python版本](https://img.shields.io/badge/Python-3.11.4-blue)

## 项目介绍

### 流程图

```mermaid
---
title: 游戏流程图
---
graph TD;
    Start[游戏开始]
    End[游戏结束]
    GameRound[游戏回合]
    PlayerRound[遍历玩家回合]
    RoundStart[回合开始]
    RoundEnd[回合结束]
    PlayerStart[玩家回合开始]
    PlayerEnd[玩家回合结束]
    SwitchPokemon[切换宝可梦（未实现）]
    UseItem[使用道具]
    Attack[攻击]
    CheckGame[检查游戏是否结束（hp=0）]


    Start --> GameRound
    GameRound --> RoundStart
    RoundStart --> PlayerRound
    PlayerRound --> PlayerStart
    PlayerStart --> Attack
    PlayerStart --> UseItem
    PlayerStart --> SwitchPokemon
    Attack --> PlayerEnd
    UseItem --> PlayerEnd
    SwitchPokemon --> PlayerEnd
    PlayerEnd --> CheckGame
    CheckGame -->|Yes| End
    CheckGame -->|No| RoundEnd
    RoundEnd --> GameRound

```

### 游戏流程介绍

### 目录结构

```bash
weijianxian
│ Basic.py       # 基础类
│ Game.py        # 游戏类
│ main.py        # 入口
│ Player.py      # 玩家类
│ Pokemon.py     # Pokemon类
│ PokemonType.py # Pokemon属性
│ readme.md      # 项目介绍
│ Skills.py      # 技能实现 (WIP)
│ Status.py      # 宝可梦状态实现(WIP)
│
├─utils
│ │ __init__.py  # 重写 print input

```

### 依赖

使用 `pip install colorama` 实现彩色输出
