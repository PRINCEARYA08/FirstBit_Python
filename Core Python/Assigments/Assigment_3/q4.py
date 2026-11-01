f_said = int(input("Enter the first number: "))
s_said = int(input("Enter the second number: "))
t_said = int(input("Enter the third number: "))

if(f_said + s_said >t_said and f_said + t_said > s_said and s_said + t_said > f_said):
    print("The triangle is valid")
else:
    print("The triangle is not valid")