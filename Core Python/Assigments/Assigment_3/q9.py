s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))

total_mark = s1 + s2 + s3 + s4 + s5
total_marks = total_mark / 5

if total_marks>90:
    print(f"{total_marks} First class")
elif total_marks>60:
    print(f"{total_marks} Second class")
elif total_marks>40:
    print(f"{total_marks} third class")
else:
    print("fail")