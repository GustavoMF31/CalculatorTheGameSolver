class Button:
    def __init__(self, func, name):
        self.func = func
        self.name = name

    def __str__(self):
        return self.name


class Mul(Button):
    def __init__(self, factor):
        super().__init__(lambda x: x * factor, f"X{factor}")


class Add(Button):
    def __init__(self, n):
        super().__init__(lambda x: x + n, f"+{n}")


class Sub(Button):
    def __init__(self, n):
        super().__init__(lambda x: x - n, f"-{n}")


class Div(Button):
    def __init__(self, n):
        super().__init__(lambda x: self.perfect_div(x, n), f"/{n}")

    @staticmethod
    def perfect_div(a, b):
        if a % b == 0:
            return a // b
        else:
            raise ValueError(f"{a} is not a multiple of {b}")


class ChangeSign(Button):
    def __init__(self):
        super().__init__(lambda x: -x, "+-")


class RemoveLastDigit(Button):
    def __init__(self):
        super().__init__(lambda x: int(str(x)[0:-1]), "<<")


class InsertDigit(Button):
    def __init__(self, n):
        super().__init__(lambda x: int(str(x) + str(n)), str(n))


class ReplaceNumber(Button):
    def __init__(self, old, new):
        super().__init__(lambda x: int(self.replace_if_possible(str(x), old, new)), f"{old}=>{new}")

    @staticmethod
    def replace_if_possible(string, old, new):
        if old in string:
            return string.replace(old, new)
        else:
            raise ValueError(f"String '{string}' does not contain '{old}' to replace")


def parse_buttons(button_symbols):
    return list(map(parse_button, button_symbols.split(" ")))


def parse_button(button_symbol):

    if button_symbol == "<<":
        return RemoveLastDigit()
    elif button_symbol == "+-":
        return ChangeSign()
    elif button_symbol.startswith("+"):
        return Add(int(button_symbol[1:]))
    elif button_symbol.startswith("-"):
        return Sub(int(button_symbol[1:]))
    elif button_symbol.startswith("X"):
        return Mul(int(button_symbol[1:]))
    elif button_symbol.startswith("/"):
        return Div(int(button_symbol[1:]))
    elif "=>" in button_symbol:
        nums = button_symbol.split("=>")

        return ReplaceNumber(nums[0], nums[1])
    else:
        return InsertDigit(int(button_symbol))