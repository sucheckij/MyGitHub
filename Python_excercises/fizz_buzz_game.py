game_number = int(input("Type a number until you want count fizz_buzz\n"))

for i in range(1,game_number+1):
    if i % 3 ==0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)
