n=7
m=5
for i in range(n):
    for j in range(m):
        if (j==2 or (i==0 and j!=2)or (i==6 and j<2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
for i in range(n):
    for j in range(m):
        if(i==0 or i==3 or i==6 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
for i in range(n):
    for j in range(m):
        if(i==0 or i==3 or i==6 or j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
i=0
j=6
for row in range(4):
    for col in range(7):
        if row==col:
            print("*", end=" ")
        elif row==i and col==j:
            print("*",end=" ")
            i=i+1
            j=j-1
        else:
            print(" ",end=" ")
    print(" ")

for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")

for i in range(6):
    for j in range(6):
        if (j==0 or j==5 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
for i in range(7):
    for j in range(5):
        if ((j==0 or j==4) and i!=0) or ((i==0 or i==3) and (j>0 and j<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")