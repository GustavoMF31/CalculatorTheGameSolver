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


def solveCTG(buttons, start, goal, max_moves):
	
	if max_moves == 0:
		 return False, None

	for button in buttons:
		try:
			next_num = button.func(start)
		except Exception as e:
			next

		if next_num == goal:
			return True, [str(button)]

		result, log = solveCTG(buttons, next_num, goal, max_moves - 1)
		
		if result == True:
			return True, ([str(button)] + log)

	return False, None


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


def main():

	buttons = parse_buttons(input("Available buttons: "))

	start = int(input("Starting value: "))
	goal = int(input("Goal: "))
	max_moves = int(input("Amount of Moves: "))

	print(" ".join(solveCTG(buttons, start, goal, max_moves)[1]))

main()