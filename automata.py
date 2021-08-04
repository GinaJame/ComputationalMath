f= open("test1.txt","r") # "r" reading mode
# Define the values
states= f.readline().rstrip('\n').split(",")  # rstrip() removes  \n at the beginning and end  split() each time there's a comma it devides
alphabet= f.readline().rstrip('\n').split(",")
initialState= f.readline().rstrip('\n')
finalStates= f.readline().rstrip('\n').split(",")
transitionTable=[['State']]  # initialize transitionTable and put State in (0,0)
for z in alphabet:
    transitionTable[0].append(z)  # amplia el arreglo con alphabet
for q in states:
    transitionTable.append([q])  # añade columnas con states

lines = [line.rstrip() for line in f]  # array that has the transitions

#Transition Table
state=1

alphabetIndex=0
for l in range(len(lines)):
    values = lines[l].split("=>")

    first = values[0].split(",")

    if transitionTable[state][0]!=first[0]:
            state+=1
            alphabetIndex = 0
    while first[1]!=alphabet[alphabetIndex]:
        transitionTable[state].append('qs')
        if alphabetIndex<len(alphabet)-1:
            alphabetIndex+=1
    if lines[l+1][0]!=first[0]:
        while alphabetIndex<len(alphabet)-1:
            transitionTable[state].append('qs')
            alphabetIndex+=1
    alphabetIndex+=1
    transitionTable[state].append(values[1])


print(transitionTable)  # [][]



#####################
counter_rename = 0

def check_lists_equal(list1, list2):
    if list1 == list2:
        return True
    return False


def belong_set_states(state, setStates):
    if setStates.count(state) !=0:
        return True
    return False


def rename_states(listStates, table, newName):
    for i in range(0,len(listStates)):
        for col in range(0,len(table)):
            for row in range(0,len(table[0])):
                if listStates[i]==table[col][row]:
                    table[col][row] = newName


def minimize(table):
    for i in range(1, len(table)-1):

        for j in range(i+1, len(table)):
            row1 = []
            row2 = []
            for n in range(1, len(table[0])):
                row1.append(table[i][n])
                row2.append(table[j][n])
                global finalStates

            equal = check_lists_equal(row1, row2)
            if equal:
                if belong_set_states(table[i][0], finalStates) == belong_set_states(table[j][0], finalStates):
                    hold_states = [table[i][0], table[j][0]]
                    global counter_rename
                    global initialState
                    new_name_state = "A" + str(counter_rename)
                    counter_rename += 1
                    check_row1In = belong_set_states(table[i][0], initialState)
                    check_row2In = belong_set_states(table[j][0], initialState)
                    check_FS =belong_set_states(table[i][0], finalStates)

                    if check_FS:
                        finalStates.remove(table[i][0])
                        finalStates[finalStates.index(table[j][0])] = new_name_state
                    if check_row1In:
                        initialState = new_name_state
                        del table[j]
                        # print(table)
                    elif check_row2In:
                        if belong_set_states(table[i][0],finalStates):
                            rename_states(table[j][0],table, new_name_state)
                        initialState = new_name_state
                        del table[i]
                        # print(table)
                    elif not (check_row1In and check_row2In):
                        del table[i]
                    rename_states(hold_states, table, new_name_state)
                    print(table) # este print se puede quitar
                    return True
    # print(table)
    return False


minimize_check = minimize(transitionTable)

while minimize_check:
    minimize_check = minimize(transitionTable)



print(transitionTable)

print(finalStates)

read_string = input()

stateRead=initialState
for i in read_string:



def look_for_State(a, table):
    for t in table:
        print(t)