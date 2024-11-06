num1: float = float(input("enter first number"))
num2: float = float(input("enter second number"))
for i in range(3):
    if num1 > num2:
        print(num1)
    else:
        print(num2)

num1: int = int(input("enter first number"))
num2: int = int(input("enter second number"))
avg_num: int = (num1 + num2) // 2
print(avg_num)

num1: int = int(input("enter first number"))
num2: int = int(input("enter second number"))
num3: int = int(input("enter third number"))
if num1 > num2 and num3:
    print(f" the first number is bigger {num1}")
elif num2 > num1 and num3:
    print(f" the second number is bigger {num2}")
elif num3 > num2 and num1:
    print(f" the third number is bigger {num3}")

movie_duration: float = int(input("enter movie duration:"))
movie_length_hours = movie_duration // 60
movie_length_minutes = movie_duration % 60
print(f"the movie is {movie_length_hours} hours and {movie_length_minutes} minutes long")

while True:
    num: int = int(input("enter a number:"))
    if 1000 <= num <= 9999:
        last_digit = num % 10
        # last_digit = str(num)
        print(f"the last digit is {last_digit}")
        break
    else:
        print("invalid number,enter a four digit number please")
        continue

while True:
    num: int = int(input("enter a number:"))
    if 1000 <= num <= 9999:
        second_to_last_digit = (num // 10) % 10
        print(f"the second to last digit is {second_to_last_digit}")
        break
    else:
        print("invalid number,enter a four digit number please")
        continue

while True:
    num: int = int(input("enter a number:"))
    if 10 <= num <= 99:
        last_digit = num % 10
        first_digit = num // 10
        print(f"the number that you get from two digits of {num} combined is {last_digit + first_digit}")
        break
    else:
        print("invalid number, enter two digit number please:")
        continue

while True:
    num: int = int(input("enter a number:"))
    if 10 <= num <= 99:
        last_digit = num % 10
        first_digit = num // 10
        print(f"the number that you get from {num} reversed is ({last_digit}{first_digit})")
        break
    else:
        print("invalid number, enter two digit number please:")
        continue

num: int = int(input("enter a number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")
