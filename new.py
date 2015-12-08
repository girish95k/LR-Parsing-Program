    __author__ = 'Aman and Kai and Girish'
    
    # Process the grammar input file
    grammar = open("grammar.txt", "r")
    pro = []
    nonter=set()
    ter=set()
    for production in grammar:
        l = list(map(lambda x: x.strip(), production.split(":")))
        pro.append(tuple(l))
        ter.update(l[1])
        nonter.update(l[0])
    ter=ter-nonter
    print(ter,nonter)
    grammar.close()
    
    # Process the table input file
    table = open("table.txt", "r")
    symbols = table.readline().rstrip().split("-")
    final = {}
    for i, rules in enumerate(table):
        values = rules.rstrip().split("-")
        for j, value in enumerate(values):
            if value != "*":
                final[str(i) + symbols[j]] = value
    table.close()
    
    inputs = open("input.txt", "r")
    for s in inputs:
        # Take the input string
        s = s.strip()
        input_string = s
        s += "$"
    
        # Begin parsing
        stack = ['$', 0]
        path = []
    
        while True:
            state = stack[-1]
            symbol = s[0]
            key = str(state) + symbol
            if key not in final:
                print("The string", input_string, "has been rejected by the grammar")
                break
            action = final[key]
            if action == 'acc':
                print("The string", input_string, "has been accepted by the grammar")
                for step in reversed(path):
                    print(step[0], "->", step[1])
                break
            elif action[0] == 'S':
                stack.append(action[1])
                s = s[1:]
            else:
                l = pro[int(action[1]) - 1]
                path.append(l)
                num = len(l[1])
                stack = stack[:-num]
                # perform goto
                key = str(stack[-1]) + str(l[0])
                if key not in final:
                    print("The string", input_string, "has been rejected by the grammar")
                    break
                goto = final[key]
                stack.append(goto)