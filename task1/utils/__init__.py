builtin_print = print  # 备份默认print函数
builtin_input = input  # 备份默认input函数
try:
    import colorama

    changeRule: list[tuple] = [
        ("[red]", colorama.Fore.RED),
        ("[green]", colorama.Fore.GREEN),
        ("[yellow]", colorama.Fore.YELLOW),
        ("[blue]", colorama.Fore.BLUE),
        ("[magenta]", colorama.Fore.MAGENTA),
        ("[cyan]", colorama.Fore.CYAN),
        ("[white]", colorama.Fore.WHITE),
        ("[/]", colorama.Fore.RESET),
    ]

except ImportError:
    print(
        "colorama没有安装，无法使用彩色输出。建议使用pip install colorama安装colorama。"
    )
    changeRule: list[tuple] = [
        ("[red]", ""),
        ("[green]", ""),
        ("[yellow]", ""),
        ("[blue]", ""),
        ("[magenta]", ""),
        ("[cyan]", ""),
        ("[white]", ""),
        ("[/]", ""),
    ]


def print(*args, **kwargs):
    """自定义print函数，支持彩色输出"""
    data = "".join(args)
    for rule in changeRule:
        data = data.replace(rule[0], rule[1])
    if not data.endswith(colorama.Fore.RESET):
        data += colorama.Fore.RESET
    builtin_print(data, **kwargs)


def input(*args, **kwargs):
    """自定义input函数，支持彩色输出"""
    data = "".join(args)
    for rule in changeRule:
        data = data.replace(rule[0], rule[1])
    return builtin_input(data, **kwargs)


def question(tip: str, requir: list = []) -> str:
    """输入函数，自定义输入要求

    :param tip: 输入提示

    :param requir: 输入要求,默认不限制

    :return: 输入结果

    """

    data = input(tip)
    if data not in requir and requir != []:
        print("[red]输入不合法，请重新输入[/]")
        return question(tip, requir)
    return data


if __name__ == "__main__":
    print("[red]红色[/]")
    data = question("[green]请输入1-3:[/]", ["1", "2", "3"])
