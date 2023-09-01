import numpy as np
import time 
from dynamic_longest_subsequence import main
from recurse_longest_subsequence import calc_position 
import matplotlib.pyplot as plt


def build_arr(p,t): 
    x = "babbababaababbbababaaabababbabaaabababbaaabababbabababbababab" # downwards -> i 
    y = "cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbbabbaaabaaababbabababababababbababababababababbababbabbababbababbababbababbabababbababbabababbabababbababababbababbabbababbbbbbababbabaaaaaababababbabbbbababababbababbababababbabababbabababababb" # vertikal -> j 
    y =10*(y+y+y+y+y+y+y+y+y)
    x = 100000*(x) 
    x = x[0:p]
    y = y[0:t]

    L = np.zeros((len(x) +1, len(y) +1))
    return L,x,y

def recursive():
    plt.figure(1)
    #bigger text 
    print("longer text...") 
    coords_rec = []
    i = 3
    while True:
        if(i >= 25):
            break
        
        L,x,y = build_arr(4,i)
        print(x)
        print(y) 
        

        anfang = time.time()
        ret = calc_position(len(x),len(y),x,y)
        print("recursive: ",ret)
        ende = time.time()
        dif = ende-anfang
        coords_rec.append((i,dif))

        i+=5


    x_coords_rec = [coord[0] for coord in coords_rec]
    y_coords_rec =  [coord[1] for coord in coords_rec]
    
 
    plt.scatter(x_coords_rec, y_coords_rec, color='red', marker='x')

    
    #bigger pattern
    print("longer pattern") 
    coords_rec = []
    i = 1
    while True:
        if(i == 7):
            break
        
        L,x,y = build_arr(i,25)
        print(x)
        print(y) 

        anfang = time.time()
        ret = calc_position(len(x),len(y),x,y)
        print("recursive: ",ret)
        ende = time.time()
        dif = ende-anfang
        coords_rec.append((i,dif))

        i+=1


    x_coords_rec = [coord[0] for coord in coords_rec]
    y_coords_rec =  [coord[1] for coord in coords_rec]
    plt.scatter(x_coords_rec, y_coords_rec, color='blue', marker='x')
    
    #both
    print("both") 
    coords_rec = []
    i = 1
    while True:
        if(i == 12):
            break
        
        L,x,y = build_arr(i,i)
        print(x)
        print(y) 

        anfang = time.time()
        ret = calc_position(len(x),len(y),x,y)
        print("recursive: ",ret)
        ende = time.time()
        dif = ende-anfang
        coords_rec.append((i,dif))

        i+=1


    x_coords_rec = [coord[0] for coord in coords_rec]
    y_coords_rec =  [coord[1] for coord in coords_rec]
    plt.scatter(x_coords_rec, y_coords_rec, color='yellow', marker='x')
    plt.title('recursive')
    plt.xlabel('X-Koordinate')
    plt.ylabel('Y-Koordinate')
    plt.grid(True)
    plt.show() 

def iterative():
    plt.figure(1)

    print("bigger text") 
    #bigger text 
    coords_dynamic = []

    i = 10
    while True:
        if(i >= 3000):
            break
        
        L,x,y = build_arr(4,i)
        
        anfang = time.time()
        main(x,y,L)
        ende = time.time()
        dif = ende-anfang
        coords_dynamic.append((i,dif))



        i+=300



    x_coords_dyn = [coord[0] for coord in coords_dynamic]
    y_coords_dyn = [coord[1] for coord in coords_dynamic]

    plt.scatter(x_coords_dyn, y_coords_dyn, color='red', marker='x')

    #bigger pattern
    print("bigger pattern") 
    coords_dynamic = []

    i = 1
    while True:
        if(i >= 3000):
            break
        
        L,x,y = build_arr(i,300)
        
        anfang = time.time()
        main(x,y,L)
        ende = time.time()
        dif = ende-anfang
        coords_dynamic.append((i,dif))



        i+=400

    x_coords_dyn = [coord[0] for coord in coords_dynamic]
    y_coords_dyn = [coord[1] for coord in coords_dynamic]
    plt.scatter(x_coords_dyn, y_coords_dyn, color='blue', marker='x')
     
    #both
    print("both") 
    coords_dynamic = []

    i = 1
    while True:
        if(i >= 3000):
            break
        
        L,x,y = build_arr(i,i)
        
        anfang = time.time()
        main(x,y,L)
        ende = time.time()
        dif = ende-anfang
        coords_dynamic.append((i,dif))



        i+=500

    x_coords_dyn = [coord[0] for coord in coords_dynamic]
    y_coords_dyn = [coord[1] for coord in coords_dynamic]
    plt.scatter(x_coords_dyn, y_coords_dyn, color='yellow', marker='x')

    
    plt.title('dynamic')
    plt.xlabel('X-Koordinate')
    plt.ylabel('Y-Koordinate')
    plt.grid(True)
    plt.show() 
iterative()
    
    
