for i in range(1,7,1):
    for j in range(0,6-i):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()