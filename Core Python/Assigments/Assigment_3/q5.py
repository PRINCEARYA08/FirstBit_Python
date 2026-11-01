cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

if(cp>sp):
    loss = cp - sp
    print(f'{loss} is your loss price ')
else:
    profit = sp - cp 
    print(f'{profit} is your loss price ')
