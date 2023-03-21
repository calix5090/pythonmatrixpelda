import random
import os

os.system('cls||clear')

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

e=1
for i in range(s):
    for j in range(o):
        matrix[i][j]=e
        e=e+1

#print(matrix)
matrix_kiir(matrix,5)
print()


ujra=True

while ujra:
    try:
        s=input("Kérek egy (1...100) egészszámot: ")
        i=int(s)
        if i>0 and i<=100 :
            ujra=False
        else:
            print("A szám nem megfelelő értékű! (újra!)")
    except ValueError:
        print("A szám nem értelmezhető! (újra!)")

print("A szám négyzete: {0}".format(i*i))
print(f"Ez egy f-szting kiírása az i változónak: {i:>9}")