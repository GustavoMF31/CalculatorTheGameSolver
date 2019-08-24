import buttons

def solveCTG(buttons, start, goal, max_moves):
    
    if max_moves == 0:
         return False, None

    for button in buttons:

        try:
            next_num = button.func(start)
        except Exception as e:
            continue

        if next_num == goal:
            return True, [str(button)]

        result, log = solveCTG(buttons, next_num, goal, max_moves - 1)
        
        if result == True:
            return True, ([str(button)] + log)

    return False, None


def main():

    available_buttons = buttons.parse_buttons(input("Available buttons: "))

    start = int(input("Starting value: "))
    goal = int(input("Goal: "))
    max_moves = int(input("Amount of Moves: "))

    solvable, solution = solveCTG(available_buttons, start, goal, max_moves)

    if solvable:
        print(" ".join(solution))
    else:
        print("Unsolvable")


if __name__ == "__main__":
    main()