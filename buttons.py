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
        super().__init__(lambda x: x / n, f"/{n}")


class ChangeSign(Button):
    def __init__(self):
        super().__init__(lambda x: -x, "+-")


class RemoveLastDigit(Button):
    def __init__(self):
        super().__init__(lambda x: int(str(x)[0:-1]), "<<")