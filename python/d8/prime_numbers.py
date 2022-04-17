#prime numbers: cac so nguyen to (chi chia het cho 1 va chinh no)

#Write your code below this line 👇
def prime_checker(number):
    compter = 0
    for n in range(2, number):
        if (number % n) == 0:
            compter += 1
    print(compter)

    if number < 2 or compter > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)