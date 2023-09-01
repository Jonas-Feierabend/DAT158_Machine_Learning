

global c
c = 0
def calc_max(i,j,x,y):
    if(i == 0 or j == 0):
        return 0
    else:
        return max(calc_position(i-1,j,x,y), calc_position(i,j-1,x,y) )
    



def calc_position(i,j,x,y):
    if( i == 0 or j == 0):
        return 0 
    global c
    c+= 1

    if(x[i-1] == y[j-1]):
        return (calc_position(i-1,j-1,x,y) +1) 
    else:
        return calc_max(i,j,x,y)


if __name__ == "__main__":
    x = "aaaaaaaaa" # downwards -> i 
    y = "ccccccccccccccc" # vertikal -> j 
    ret = calc_position(len(x), len(y),x,y) 
        
        
    print(ret)
    print("recursions: ",c); 
