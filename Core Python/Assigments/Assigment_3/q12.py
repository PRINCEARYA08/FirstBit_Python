num = int(input("Enter a number: "))
#while(num>0):

a=num%10
num=num//10

b=num%10
num=num//10

c=num%10
num=num//10

#print(a,end=" ")
#print(b,end=" ")
#print(c)

if a == c:
    print("Number is Palindrom")
else:
    print("Number is not Palindrom")
