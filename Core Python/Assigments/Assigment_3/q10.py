male = int(input("Enter male age: "))
female =  int(input("Enter female age: "))

if(male>21 and female>18):
    print("Eigible to marry")
elif(male<21):
    print("male is not eligible")
elif(female<18):
    print("female is not eligible")
else:
    print("both are not elibible")
