#Write your code below this line 👇

def prime_checker(number):
    if number == 1:
        print("1 it's not prime or composite number")
    else:
        count = 0
        for n in range(1,number+1):
            if number % n == 0:
                count += 1
                if count > 2:
                    break
        if count > 2:
            print("It's not a prime number.")
        else:
            print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
