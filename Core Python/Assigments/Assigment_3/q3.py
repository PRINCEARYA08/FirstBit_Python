angle1 = int(input("Enter the first angle of triangle: "))
angle2 = int(input("Enter the second angle of triangle: "))
angle3 = int(input("Enter the third angle of triangle: "))

total_angle = angle1 + angle2 + angle3

if total_angle == 180:
    print("The triangle is valid")
else:
    print("The triangle is not valid")