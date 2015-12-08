import pico

def hello(productions="default"):
    f=open("grammar1.txt","w")
    f.write(productions)
    f.close()
    ter=set()
    nonter=set()
    productions=productions.split("\n")[:-1]
    for production in productions:
	    print("P",production)
	    head,body=production.split(":")
	    nonter.update(head)
	    ter.update(body)
    ter=ter-nonter
    response=""
    for item in ter:
        response+=item+" "
    response+="$ \n"
    for item in nonter:
        response+=item+" "
    return response
	
def savetable(rules="default"):
    print("HERE")
    f=open("table1.txt","w")
    rules=rules.split("\n")
    for rule in rules:
	    f.write(rule[:-1]+"\n")
    f.close()
    return "Cool"
def saveinput(inputs="default"):
    f=open("input1.txt","w")
    f.write(inputs)
    f.close()
    return "WOW"
"""
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
        results+="Attempting to parse "+input_string+"\n\n\n"
        while True:
            state = stack[-1]
            symbol = s[0]
            results+="STACK has :"+str(stack)+"\n\n"
            results+="Processing :"+s+"\n\n"
            key = str(state) + symbol
            if key not in final:
                results+="The string "+input_string+" has been rejected by the grammar\n\n\n\n"
                break
            action = final[key]
            if action == 'acc':
                results+="The parsing steps are \n\n"
                for step in reversed(path):
                    results+=step[0]+"->"+step[1]+"\n"
                results+="The string "+input_string+" has been accepted by the grammar\n\n\n\n"
                break
            elif action[0] == 'S':
                results+="Shift move,push "+action[1]+" onto the stack\n"
                stack.append(action[1])
                s = s[1:]
            else:
                l = pro[int(action[1]) - 1]
                results+="Reduce move , pop "+str(len(l))+" symbols from the stack corresponding to "+action+"\n"
                path.append(l)
                num = len(l[1])
                stack = stack[:-num]
                # perform goto
                state=str(stack[-1])
                symbol=str(l[0])
                key = str(stack[-1]) + str(l[0])
                if key not in final:
                    results+="The string "+input_string+" has been rejected by the grammar\n"
                    break
                goto = final[key]
                results+="Perform GOTO move of "+state+" , "+symbol +" by pushing "+goto+"\n"
                stack.append(goto)
    print(results)
    return results
"""

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
        results+="Attempting to parse "+input_string+"\n\n\n"
        while True:
            state = stack[-1]
            symbol = s[0]
            results+="STACK has :"+str(stack)+"\n\n"
            results+="Processing :"+s+"\n\n"
            key = str(state) + symbol
            if key not in final:
                results+="The string "+input_string+" has been rejected by the grammar\n\n\n\n"
                break
            action = final[key]
            if action == 'acc':
                results+="The parsing steps are \n\n"
                for step in reversed(path):
                    results+=step[0]+"->"+step[1]+"\n"
                results+="The string "+input_string+" has been accepted by the grammar\n\n\n\n"
                break
            elif action[0] == 'S':
                results+="    Shift move,push "+action[1]+" onto the stack\n"
                stack.append(action[1])
                s = s[1:]
            else:
                l = pro[int(action[1]) - 1]
                if(l[1]!='#'):
                    results+="    Reduce move , pop "+str(len(l[1]))+" symbols from the stack corresponding to "+action+" and push head of production: "+str(l[0])+"\n"
                    num = len(l[1])
                    stack = stack[:-num]
                else:
					results+="    Reduce move , pop 0 symbols from the stack corresponding to "+action+"\n"
                path.append(l)
                # perform goto
                state=str(stack[-1])
                symbol=str(l[0])
                key = str(stack[-1]) + str(l[0])
                if key not in final:
                    results+="The string "+input_string+" has been rejected by the grammar\n"
                    break
                goto = final[key]
                results+="Perform GOTO move of "+state+" , "+symbol +" by pushing "+goto+"\n"
                stack.append(goto)
    print(results)
    return results
