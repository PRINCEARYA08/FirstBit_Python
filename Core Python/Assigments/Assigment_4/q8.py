num = int(input("Enter the number :"))
count=0
for i in range(1,num+1):
    if(i%5==0 and i%7==0 ):
        print(i)
        count+=1
print("count of numbers is",count)