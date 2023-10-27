import copy 
"""config"""
I = [[2,3], [4,3], [3,4], [3,3], [4,7]] # items (size, value) 
B = 7  #backpack size
remove_dominating = True





""" remove dominating function"""
def remove_dominating(A,j): 
    new_A = copy.deepcopy(A[j] ) 

    i = 0
    for first in A[j]:
        m= 0
        for second in A[j]:
            if(m != i and first[0] <= second[0] and first[1] >= second[1]):
                    if second in new_A: 
                        new_A.remove(second)
                
            m+=1
        i+=1

    A[j] = copy.deepcopy(new_A) 
        


"""initialising memory"""
A = []# memory



"""start with j = 0"""
A = [[] for _ in range(len(I)) ]
A[0].append([0,0]) # choosing no item
A[0].append(I[0]) # chosing the first item 

print("A[",1,"]")
print("Before: ", A[0])
print("After: ", A[0])
print("\n") 
 

"""consider more items """
for j in range(1,len(I)):
    A[j] = copy.deepcopy(A[j-1])# you can choose to not take the new item 


    #you can combine the new item (with no other item or with a combination) 
    for pair in A[j-1]:
   
        new_size = pair[0] + I[j][0] # add weight of old subset and new item
        if(new_size <= B): # does it fit into backpack?
            #add new subset
            new_set = [new_size, pair[1] + I[j][1]] # combine new item with old subset
            A[j].append(new_set)



    #remove dominating
    print("A[",j+1,"]")
    print("Before: ", A[j])
    remove_dominating(A, j)
    print("After: ", A[j])
    print("\n")


best = 0
for e in A[-1]:
    if(e[1] > best):
        best = e[1]

print("Best result is: ", best) 



