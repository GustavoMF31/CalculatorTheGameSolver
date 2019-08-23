import copy

class Button:
	def __init__(self, func, name):
		self.func = func
		self.name = name

	def __str__(self):
		return self.name


class Mul(Button):
	def __init__(self, factor):
		self.func = lambda x: x * factor
		self.name = f"X{factor}"


class Add(Button):
	def __init__(self, n):
		self.func =lambda x: x + n
		self.name = f"+{n}"


class Sub(Button):
	def __init__(self, n):
		self.func = lambda x: x - n
		self.name = f"-{n}"


class Div(Button):
	def __init__(self, n):
		self.func =lambda x: x / n
		self.name = f"/{n}"


class CS(Button):
	def __init__(self):
		self.func =lambda x: -x
		self.name = f"+-"


class RemoveLastDigit(Button):
	def __init__(self):
		self.func =lambda x: int(str(x)[0:-1])
		self.name = f"<<"


def solveCTG(buttons, start, goal, max_moves = 10, log = None):

	if log == None:
		log = []
	
	if max_moves == 0:
		 return False, log

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

	return False, log

def main():
	buttons = [
		Mul(3),
		Div(5),
		RemoveLastDigit()
	]

	start = 50
	goal = 9
	max_moves = 4

	print(" ".join(solveCTG(buttons, start, goal, max_moves)[1]))

main()