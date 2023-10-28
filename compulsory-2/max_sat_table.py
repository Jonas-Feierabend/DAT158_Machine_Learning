clauses = [
        [1,2],
        [1,3],
        [1,2,3,4]
    ]
""" initialise memory"""
max_num = 0
for arr in clauses:
    for elem in arr:
        max_num = elem if elem>max_num else max_num
clauses_num = len(clauses)

#x1, x2, x3 C1 C2 C3 T
#0,  0   0   1  1  1  3

memory = [[ 0 for _ in range(0,max_num+clauses_num+1) ] for _ in range(0,2**max_num)]

max_bin_length = len(bin((2**max_num)-1)[2:])
i = 0
for row in memory:
    # add True false 
    binary = bin(i)[2:]
    while len(binary) < max_bin_length:
        binary = '0' + binary

    j= 0 
    for c in binary:
        row[j] = int(c) 
        j+=1
    

    # calculate
    for clause in clauses
        answ = 0
        for faktor in clause:
            answ += 1
        row[j] = 
        j+=1 

    i+=1
    


for row in memory:
    print(row) 
