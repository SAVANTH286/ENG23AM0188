n=5
print("n*n pattern")
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print("")
print("left triangle")
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("")
print("right triangle")
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
print("inverted right triangle")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print(" ")
