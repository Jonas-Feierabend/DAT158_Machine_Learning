import random
"""clauses """ 
clauses = [
        [1,[1,2]], # [Faktor, [1 -> x1; 2-> x2; -1 -> not x1 ] 
        [2,[-1,3]],
        [1, [1,2,3,4]]
    ]
def fancy_printing(clause):
    i= 0
    middle = ""
    for part in clause:
        if(i != 0) :
            middle += " or "

        if(part < 0):
            middle += "not " 
        middle += "x"
        middle += str(abs(part) ) 
        middle += " " 
        i+=1 
    print("clause", clause[0],"*(", middle, ")", ":", res)

""" initialise memory"""
max_num = 0
for arr in clauses:
    for elem in arr[1]:
        max_num = elem if elem>max_num else max_num
clauses_num = len(clauses)
x = []
for i in range(0,max_num): 
    x.append(random.randint(0,1) ) 
print("Random x: ", x) 

""" calculate c1, c2,..."""
total = 0 
for clause in clauses:
    res = 0
    for part in clause[1]:
        if(part > 0):
            if(x[part-1] == 1):
                res = 1
                break
        elif(part < 0) :
            if(x[(-part)-1] == 0):
                res = 1
                break
    res = res * clause[0]
    total += res
    fancy_printing(clause[1]) 

print("total: ", total ) 
