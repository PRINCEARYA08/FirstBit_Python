num = int(input("Enter the number :"))
count=0
for i in range(1,num+1):
    if(i%2==0 or i%3==0 ):
        continue
    #elif(i%5==0):
      #  continue
    else:
        print(i)
        count+=1
print("count of numbers is",count)