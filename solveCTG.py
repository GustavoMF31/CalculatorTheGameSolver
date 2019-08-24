import buttons

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
		return buttons.RemoveLastDigit()
	elif button_symbol == "+-":
		return buttons.ChangeSign()
	elif button_symbol.startswith("+"):
		return buttons.Add(int(button_symbol[1:]))
	elif button_symbol.startswith("-"):
		return buttons.Sub(int(button_symbol[1:]))
	elif button_symbol.startswith("X"):
		return buttons.Mul(int(button_symbol[1:]))
	elif button_symbol.startswith("/"):
		return buttons.Div(int(button_symbol[1:]))


def main():

	buttons = parse_buttons(input("Available buttons: "))

	start = int(input("Starting value: "))
	goal = int(input("Goal: "))
	max_moves = int(input("Amount of Moves: "))

	print(" ".join(solveCTG(buttons, start, goal, max_moves)[1]))

main()