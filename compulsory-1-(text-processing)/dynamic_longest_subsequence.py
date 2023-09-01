import numpy as np 

def build_arr(): 
    """this function builds the table for the common longest
    subsequence algorithm"""
    x = "babbabab" # downwards -> i 
    y = "bbabbaaab" # vertikal -> j 

    L = np.zeros((len(x) +1, len(y) +1))
    return L,x,y


def calc_max(i,j,L):
    """this function returns the bigger value of the 
    cell above and the cell to the left, the cells 
    on the border are defined with 0 """
    if(i == 0 or j == 0):
        return 0
    else: 
        return max(L[i-1][j], L[i][j-1])

def main(x,y,L): 
    """This function filles out the table, to calculate the common longest subsequence.
    The answer can be found in the most right-bottom cell"""
    i = 1 
    for row in x:

        j = 1 
        for column in y:
            if(y[j-1] == x[i-1]):
                L[i][j] = L[i-1][j-1] +1 

            else:
                L[i][j] = calc_max(i,j,L)

            j+= 1

        i+=1 
    print("iterative subsequence = ", L[-1][-1])
        

if __name__ == "__main__":
    L,x,y = build_arr()

    main(x,y,L)
