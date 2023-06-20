# 윤년이 아닐 때 1월 1일과 12월 31일의 날짜 차이는 364일 이다.
# 364 를 7 로 나누면 0으로 나누어 떨어지며, 이는 1월 1일의 요일과 12월 31일의 요일이 같다는 뜻이다.
# 1월 1일이 금요일이라면 같은 해의 마지막 금요일은 12월 31일이 되고,
# 같은 원리로 1월 1일이 각각 토요일, 일요일이라면 마지막 금요일은 12월 30일, 12월 29일이 된다.

day = input("Enter the day of the week of January 1st: ")
lst = ["Fri", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]

for i in range(len(lst)):
    if day == lst[i]:
        print("The date of film festival is {date}, 12".format(date=31 - i))
