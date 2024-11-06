number: int = 0
while True:
    num: int = int(input("enter a number:"))
    if num == -99:
        if number == 0:
            print(None)
            break
        else:
            break
    else:
        number = num + number
if number >= 1:
    print(f"the summary of numbers that you entered is {number}")

biggest_number: int = 0
smallest_number: int = 0
while True:
    num: int = int(input("enter a number:"))
    if num == 0 or num < 0:
        if biggest_number == 0:
            print(None)
            break
        else:
            break
    else:
        if smallest_number == 0 or num < smallest_number:
            smallest_number = num
        if biggest_number == 0 or num > biggest_number:
            biggest_number = num
if biggest_number >= 1:
    print(f"the biggest number is {biggest_number}")
    print(f"the smallest number is {smallest_number}")

biggest_input: int = 0
for num in range(5):
    number: int = int(input("enter a number:"))
    if num >= number:
        biggest_input = num

print(f"the biggest number is in input number {biggest_input}")
