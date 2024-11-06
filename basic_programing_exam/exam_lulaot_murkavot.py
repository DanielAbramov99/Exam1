import statistics

stop: str = "wrong data"
counter: int = 0
temp_list: list[float] = []
while True:
    try:
        temp_user: float = float(input("enter temperature:"))
        if not -5 <= temp_user <= 40:
            print(stop)
            break
        if len(temp_list) >= 1 and temp_user == 0 and temp_list[-1] == 0:
            continue
        else:
            temp_list.append(temp_user)
            counter += 1
        if counter == 12:
            break
    except ValueError:
        print("illegal parameter,try again")
if counter == 12:
    print(temp_list)
    print("correct data")
    print(f"the average annual temperature is {statistics.mean(temp_list)}")
    print(f"the biggest temperature is {max(temp_list)}")
    print(f"the smallest temperature is {min(temp_list)}")
