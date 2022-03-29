height = float(input("What is your height in cm: "))
if height > 120 : 
    age = int(input("What is your age: "))
    if age < 12 :
        print("You can ride the rollercoaster. Please pay 5$")
    elif age < 18 :
        print("You can ride the rollercoaster. Please pay 7$")
    else :
        print("You can ride the rollercoaster. Please pay 12$")
else :
    print("Sorry, you have to grow taller before you can ride")