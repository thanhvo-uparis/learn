height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
bmi = round(weight / (height ** 2), 1)
if float(bmi)<18.5 :
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>= 18 & bmi<=25 :
    print(f"Your BMI is {bmi}, you are a normal weight.")
elif bmi>=25 & bmi<=30 :
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>=30 & bmi<=35 :
    print(f"Your BMI is {bmi}, you are obese.")