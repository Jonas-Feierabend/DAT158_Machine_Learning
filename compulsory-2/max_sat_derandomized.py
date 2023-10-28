clauses = [
        [1,[1,2]], # [Faktor, [1 -> x1; 2-> x2; -1 -> not x1 ] 
        [2,[-1,3]],
        [1, [1,2,3,4]]
    ]
    
    
clauses =[
    [3,[1,-2,3]],
    [4,[1,-3]],
    [1,[-1,2,-5]], 
    [3,[-1,3]], 
    [2,[2,-4]], 
    [7,[-2,5,9]], 
    [2,[3,-4]], 
    [3,[-4,-5,21]], 
    [5,[5,-12]], 
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

answer = "" 
# x1, x2, x3 ,...
is_true = []
for x in range(1,max_num+1):
    if(x == 6): 
        break 
    print("calculating x",x) 
    
    true_val = 0 
    false_val = 0 
    for clause in clauses: 
        independent_parts = 0 
        for part in clause[1]: 
            if abs(part) > x: 
                independent_parts += 1 
        possibilities = 2** (independent_parts) 
        if(clause in is_true): 
            print("already true ", clause ) 
            true_val += clause[0]
            false_val += clause[0]
        # x not contained 
        elif ((x not in clause[1] and -x not in clause[1])):
            print("not contained", clause) 
            
            """what to do here"""
            #true_val +=val * clause[0]
            #false_val += val * clause[0]
             
        else:   
            positive_val = clause[0]  
            negative_val = clause[0] * (possibilities-1)/possibilities 
            
            if(x in clause[1]):
                
                true_val += positive_val
                false_val += negative_val
            else: 
                true_val += negative_val
                false_val += positive_val
        
            print(clause, positive_val, negative_val) 
        
    # add clauses to false/true 
    l1 = [] # x is positive 
    l2 = []  # x is negative 
    for clause in clauses:
        if(x in clause[1]):
            l1.append(clause) 
        elif(-x in clause[1]): 
            l2.append(clause) 
    print("true: ", true_val , "false: ", false_val) 
    if(true_val > false_val): 
         is_true = is_true + l1
         print("Deciding x", x , "is true") 
         answer+= "x"+str(x) + "true "
    else:
        is_true = is_true +l2
        print("Deciding x", x , "is false")   
        answer+= "x"+str(x) + "false "        
        
    print("\n") 

print(answer) 