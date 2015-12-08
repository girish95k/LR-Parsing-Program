
def lrparse():
    # Process the grammar input file
    grammar = open("grammar1.txt", "r")
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
    table = open("table1.txt", "r")
    symbols = table.readline().rstrip().split("-")
    final = {}
    for i, rules in enumerate(table):
        values = rules.rstrip().split("-")
        for j, value in enumerate(values):
            if value != "*":
                final[str(i) + symbols[j]] = value
    table.close()
    results=""
    inputs = open("input1.txt", "r")
    for s in inputs:
        # Take the input string
        s = s.strip()
        input_string = s
        s += "$"
    
        # Begin parsing
        stack = ['$', 0]
        path = []
        results+="Attempting to parse "+input_string+"</br></br></br>"
        while True:
            state = stack[-1]
            symbol = s[0]
            results+="STACK has :"+str(stack)+"</br></br>"
            results+="Processing :"+s+"</br></br>"
            key = str(state) + symbol
            if key not in final:
                results+="The string "+input_string+" has been rejected by the grammar</br></br></br></br>"
                break
            action = final[key]
            if action == 'acc':
                results+="The parsing steps are </br></br>"
                for step in reversed(path):
                    results+=step[0]+"->"+step[1]+"</br>"
                results+="The string "+input_string+" has been accepted by the grammar</br></br></br></br>"
                break
            elif action[0] == 'S':
                results+="Shift move,push "+action[1]+" onto the stack</br>"
                stack.append(action[1])
                s = s[1:]
            else:
                l = pro[int(action[1]) - 1]
                if(l[1]!='#'):
                    results+="Reduce move , pop "+str(len(l))+" symbols from the stack corresponding to "+action+"</br>"+str(l)+"\n"
                    num = len(l[1])
                    stack = stack[:-num]
                path.append(l)
                # perform goto
                state=str(stack[-1])
                symbol=str(l[0])
                key = str(stack[-1]) + str(l[0])
                if key not in final:
                    results+="The string "+input_string+" has been rejected by the grammar</br>"
                    break
                goto = final[key]
                results+="Perform GOTO move of "+state+" , "+symbol +" by pushing "+goto+"</br>"
                stack.append(goto)
    print(results)
    return results
lrparse()