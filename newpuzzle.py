arrlist = []

def move(board, goal, v):
    a = board.index(0)  # Note: We search for the integer 0, not the string '0'
    options = {}

    if a - 3 > -1:  # top
        l1 = board[:]
        temp = l1[a - 3]
        l1[a - 3] = 0
        l1[a] = temp
        if l1 not in arrlist:
            options["top"] = l1
            arrlist.append(l1)

    if a not in [2, 5, 8]:  # right
        l4 = board[:]
        temp = l4[a + 1]
        l4[a + 1] = 0
        l4[a] = temp
        if l4 not in arrlist:
            options["right"] = l4
            arrlist.append(l4)

    if a + 3 < 9:  # bottom
        l2 = board[:]
        temp = l2[a + 3]
        l2[a + 3] = 0
        l2[a] = temp
        if l2 not in arrlist:
            options["bottom"] = l2
            arrlist.append(l2)

    if a not in [0, 3, 6]:  # left
        l3 = board[:]
        temp = l3[a - 1]
        l3[a - 1] = 0
        l3[a] = temp
        if l3 not in arrlist:
            options["left"] = l3
            arrlist.append(l3)

    solve(options, goal, v)

def solve(options, goal, v):
    if not options:  # No more states to explore
        print("No solution found.")
        return

    c = []
    for side, state in options.items():
        if state != goal:
            count = v
            for j in range(9):
                if state[j] != goal[j]:
                    count += 1
            c.append(count - 1)
        else:
            print(side, "==>", v, "+0")
            for k in range(0, 9, 3):
                print(state[k], state[k + 1], state[k + 2], sep=" ", end="\n")
            print("Goal state found")
            print("Number of states", v)
            return

    best_option = min(options, key=lambda x: c[list(options.keys()).index(x)])
    print(best_option, "==>", v, "+", c[list(options.keys()).index(best_option)])
    for i in range(0, 9, 3):
        print(options[best_option][i], options[best_option][i + 1], options[best_option][i + 2], sep=" ", end="\n")
    v += 1
    move(options[best_option], goal, v)

initial = input("Initial state: ").split(",")
goal = input("Goal state: ").split(",")

# Convert input to integers
initial = [int(x) for x in initial]
goal = [int(x) for x in goal]

move(initial, goal, 1)
