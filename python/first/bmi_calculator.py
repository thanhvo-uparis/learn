#height = input("Enter your height in m: ")
#ValueError: invalid literal for int()
#print((int(height)))

height = input("Enter your height: ")
weight = input("Enter your weight: ")
bmi = int(weight) / (float(height) ** 2)
#print(round(bmi))
#or 
print(int(bmi))
