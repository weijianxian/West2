# Task 1

### 学习内容

Python基础语法、认识生成式AI

### 疑问解答

- 是否需要好的显卡？

学习人工智能有一个好的显卡会有一定帮助，但是不是刚需，你完全可以使用[Colab](https://colab.research.google.com/)或者gpu云服务器来进行机器学习代码的编写和运行

### 考核内容

#### 1. 配置环境

- 魔(ti)法(zhi)的使用

- 安装IDE集成开发环境

初学者可以选择使用[PyCharm](https://www.jetbrains.com.cn/pycharm/), 可以[申请学生免费许可证](https://blog.jetbrains.com/zh-hans/blog/2022/08/24/2022-jetbrains-student-program/)以使用专业版

个人更建议使用[VSCode](https://code.visualstudio.com/)（主要是PyCharm的Jupyter notebook太过难用， 建议初学者可以多使用Jupyter来编写程序）

- 安装Conda环境

使用[miniconda](https://docs.anaconda.com/miniconda/)就可以了,当然如果你不喜欢conda这样会污染命令窗口，使用pyenv或venv也都是可以的

- 学习python虚拟环境的配置

初学者一定要注意这个问题，从一开始就养成好的习惯

#### 2. 推荐教程

- python基础：

1. Crossin编程教室 [Python 入门指南 (python666.cn)](https://python666.cn/cls/lesson/list/)
2. Python - 100天从新手到大师的前10节课 [jackfrued/Python-100-Days: Python - 100天从新手到大师 (github.com)](https://github.com/jackfrued/Python-100-Days)
3. Python官方文档 [3.10.7 Documentation (python.org)](https://docs.python.org/zh-cn/3/)
4. 菜鸟教程 [Python3 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-tutorial.html)
5. 廖雪峰的官⽅教程 [Python教程 - 廖雪峰的官方网站 (liaoxuefeng.com)](https://www.liaoxuefeng.com/wiki/1016959663602400)
6. B站上有大量的入门基础课程，大家可以自行探索，找到适合自己的是最好的
7. 如果你想要系统的学习的话，我强烈推荐来自UCB的神课[CS61A](https://csdiy.wiki/%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8/Python/CS61A/)（课程难度较大，建议可以先选择一个更为友好的入门编程课程入门， 需要学习相关学习资料的话可以来群里问）

- 生成式AI认识：

[李宏毅2024 B站](https://www.bilibili.com/video/BV1BJ4m1e7g8/?spm_id_from=333.337.search-card.all.click&vd_source=e3594664d709db7578f4b2e76329df18)

[李宏毅2024 油管](https://www.youtube.com/watch?v=AVIKFXLCPY8&t=1s)

#### 3. 检验学习内容

在你完成python基础的知识学习后，你需要确保你对以下知识点能正确回答（如果不能你仍可以通过b站视频以及网上文档的方式进行弥补）

- 数据结构List,Dict的使用
- Lambda匿名函数
- Decorator装饰器
- 类Class，Magic Methods的使用
- re正则表达式的使用
- 列表推导式
- generator生成器（yield关键字）
- OOP面向对象编程思想
- Type Hint 类型注释

你可以写一个文档详细解释这些内容以加深印象（可以使用markdown/jupyter的形式编写）

在完成生成式AI认识的学习后，你可以写一个文档详细向我们介绍一下一个大型语言模型训练的基本步骤

#### 4. 完成作业

- ##### 作业一 宝可梦回合制对战游戏

本轮作业你将要实现一个基于命令行游玩的宝可梦对战游戏, 玩家和电脑可以各自选择3名宝可梦（电脑随机选择）组成队伍，游戏开始时候从3个宝可梦中选择一个出战，每个宝可梦拥有以下特性：

1. HP：此宝可梦的血量，当宝可梦的剩余HP小于等于0时，该宝可梦会【昏厥】
2. 属性： 宝可梦的属性会影响属性和抗性，相同属性的宝可梦会有一个相同的属性被动，宝可梦的属性会影响造成和受到的伤害
3. 攻击力：决定其对其他宝可梦的伤害
4. 防御力：来自其他宝可梦的伤害需要减去防御力的数值
5. 闪避率：在战斗中成功躲闪开敌人攻击的概率

| 属性 | 克制 | 被克制 | 属性被动                             |
| ---- | ---- | ------ | ------------------------------------ |
| 草   | 水   | 火     | 每回合回复 10% 最大HP值              |
| 火   | 草   | 水     | 每次造成伤害，叠加10%攻击力，最多4层 |
| 水   | 火   | 电     | 受到伤害时，有50%的几率减免30%的伤害 |
| 电   | 水   | 草     | 当成功躲闪时，可以立即使用一次技能   |
| ···  | ···  | ···    | ··· （你还可以自行设计）             |

被克制的宝可梦受到来自克制的宝可梦的伤害翻倍，被克制的宝可梦对克制的宝可梦造成的伤害减半

6. 招式：即技能，用来攻击对手的宝可梦，或者给对手的宝可梦附加各种各样的"效果"

这是我设计的4个宝可梦：

1. **皮卡丘（PikaChu)**

![](./阶段1.assets/BE1707F2-C858-4085-8A9C-1C282825D0D1.jpeg)

**HP**: 80 **攻击力**: 35 **防御力**: 5 **属性**: 电 **躲闪率**: 30%

**十万伏特 (Thunderbolt)：**对敌人造成 1.4 倍攻击力的电属性伤害，并有 10% 概率使敌人麻痹

**电光一闪 (Quick Attack)：**对敌人造成 1.0 倍攻击力的快速攻击（快速攻击有几率触发第二次攻击），10% 概率触发第二次

2. **妙蛙种子 (Bulbasaur)**

![](./阶段1.assets/3A370008-CF12-4404-B088-634C466404AA.jpeg)

**HP**: 100 **攻击力**: 35 **防御力**: 10 **属性**: 草 **躲闪率**: 10%

**种子炸弹 (Seed Bomb)：**妙蛙种子发射一颗种子，爆炸后对敌方造成草属性伤害。若击中目标，目标有15%几率陷入“中毒”状态，每回合损失10%生命值

**寄生种子 (Parasitic Seeds)：**妙蛙种子向对手播种，每回合吸取对手10%的最大生命值并恢复自己, 效果持续3回合

3. **杰尼龟（Squirtle）**

![傑尼龜| 寶可夢圖鑑| The official Pokémon Website in Taiwan](./阶段1.assets/D9506539-335B-4856-9768-27203069DE8C.jpeg)

**HP**: 80 **攻击力**: 25 **防御力**: 20 **属性**: 水 **躲闪率**: 20%

**水枪 (Aqua Jet)：**杰尼龟喷射出一股强力的水流，对敌方造成 140% 水属性伤害

**护盾 (Shield)：**杰尼龟使用水流形成保护盾，减少下一回合受到的伤害50%

4. **小火龙（Charmander）**

   ![](./阶段1.assets/A46CDBFA-F132-4DC0-BCCE-4506CB07B905.jpeg)

**HP**: 80 **攻击力**: 35 **防御力**: 15 **属性**: 火 **躲闪率**: 10%

**火花 (Ember)：**小火龙发射出一团小火焰，对敌人造成 100% 火属性伤害，并有10%的几率使目标陷入“烧伤”状态（每回合受到10额外伤害， 持续2回合）

**蓄能爆炎 (Flame Charge )：**小火龙召唤出强大的火焰，对敌人造成 300% 火属性伤害，并有80%的几率使敌人陷入“烧伤”状态，这个技能需要1个回合的蓄力，并且在面对改技能时敌法闪避率增加 20%

你仍需要再设计至少一个宝可梦，如果你对我设计的宝可梦不满意，feel free去修改他们

你需要实现类似这样命令行输出用于游玩该游戏：

```
请选择3个宝可梦用于组成你的队伍：
1.皮卡丘(电属性) 2.妙蛙种子(草属性) 3.杰尼龟(水属性) 4.小火龙(火属性)
输入数字选择你的宝可梦: 1 2 4

请选择你的宝可梦:
1. 小火龙 (火属性) 2. 杰尼龟 (水属性) 3. 妙蛙种子 (草属性)
输入数字选择你的宝可梦: 1
你选择了 小火龙!
电脑选择了 杰尼龟!

你的 小火龙 的技能:
1. 火花
2. 蓄能爆炎
选择一个技能进行攻击: 1
小火龙 使用了 火焰喷射!
杰尼龟 受到了 30 点伤害！剩余 HP: 70

杰尼龟 使用了 水枪!
小火龙 受到了 25 点伤害！剩余 HP: 75
```

对于我设计的玩法不满意，同样feel free去修改他们

要尽可能避免代码重复，可以创建一个Pokemon的基类，一个属性类像WaterPokemon继承自它，再有一个宝可梦继承自属性类

完成后写一个README.md文件介绍玩法，一同上传github

> 在[示例代码](./example)文件夹中有示例代码（已经实现了一个宝可梦，你们只需要在我的基础上添加更多内容就可以）（阅读代码也是一个需要大家多多锻炼的技能），大家都可以发挥自己的创造力去实现更多的功能做的fancy一点，到时候再写一个markdown文档可以放在你的github仓库下

> 我的代码里面依旧有许多不足的地方，你们可以多多完善，当然你们也可以自行从零开始设计（在面向对象程序设计中每个人都会有不一样的思路，而每个思路都会有可取的地方，大家也可以在群里多多交流）

### 作业要求

1. 不要抄袭
2. 遇到不会可以多使用搜索引擎，实在没有找到解决方法可以来群里提问，作为一个CSer学习问问题的方式也非常重要，强烈建议阅读[别像弱智一样提问](https://github.com/tangx/Stop-Ask-Questions-The-Stupid-Ways/blob/master/README.md)这篇文章
3. 不限制使用chatgpt等大语言模型工具，但你需要确保你了解模型生成的内容的每一个细节，最好你可以在使用大语言模型生成的代码部分注释上reference from chatgpt这样的内容
4. 你还需要学习基本的git的使用，所有考核都采用git的方式进行上传
5. 作业内容可能会进行更新，请保持关注

### 作业提交方式

1. 你需要学习github的使用，创建一个你自己的仓库用来存放你的代码实现
2. 接着你需要如何使用git进行pr操作，在[solutions](https://github.com/west2-online-reserve/collection-ai/blob/main/task1/solutions.md)中填写你的仓库地址，这样便于你对你的实现进行更新

相关教程

<https://github.com/west2-online-reserve/collection-ai> 里面有git使用和西二作业提交教程

[Git工作流和核心原理 | GitHub基本操作 | VS Code里使用Git和关联GitHub](https://www.bilibili.com/video/BV1r3411F7kn/?share_source=copy_web&vd_source=31019e44b62a4369d4eab7afea0fcfdf)

### Bonus

完成CS61A的学习，完成相应的作业和lab（不要畏惧全英文的学习，你完全可以使用各类翻译软件帮助你学习(包括gpt)）,如果能啃下这门课那么你的编程水平将会超过绝大多数毕业生
