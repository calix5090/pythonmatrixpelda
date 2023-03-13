import random

def matrix_kiir(m,space=3):
    s=len(m)
    o=len(m[0])
    #print ("sor =", s)
    #print("oszlop =", o)

    for i in range(s):
        for j in range(o):
            print("{0:^{1}}".format(m[i][j],space),end="") 
        print()


s=3
o=4
 
matrix=[[0]*o for i in range(s)]

e=10
for i in range(s):
    for j in range(o):
        matrix[i][j]=e
        e=e+1

#print(matrix)
matrix_kiir(matrix,5)