f= open("test1.txt","r") # "r" reading mode
# Define the values
nonTerminalSimbols = f.readline().rstrip('\n').split(",")  # rstrip() removes  \n at the beginning and end  split() each time there's a comma it devides
terminalSimbols = f.readline().rstrip('\n').split(",")
startSimbol = str(f.readline().rstrip('\n'))
productions = [line.rstrip() for line in f]

stringToEvaluate = input("String to evaluate: ")

Q = []
T=[]
indexT=0
Q.append(startSimbol)
T.append([startSimbol])
A=''
finish = False
while(not finish):
    q=Q.pop()
    i= 0
    done = False
    if len(q) != 1:
        find = False
        x=0
        u = ''
        while(not find):
            if(not q[x].isupper()):
                u = u + q[x]
            else:
                A = q[x]
                find = True
        v = q[x:]
    while(not done):
        rule = False
        for g in range(i,len(productions)):
            if(productions[g]==A):
                rule = True
                j = g
                break
        if(rule):
            w = productions[j].split('->')[1]
            upper = False
            prefixMatch = True
            q2 = u + w + v
            for g2 in q2:
                if g2.isupper():
                    upper = True
            for h in range(len(u)):
                if u[h] != stringToEvaluate[h]:
                    prefixMatch = False
            if(upper and prefixMatch):
                    Q.append(u + w + v)
                    T[indexT].append()
            i=j
    if Q.isEmpty:
        finish:True

    finish = True
