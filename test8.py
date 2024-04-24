answer = 8
guess = int(input("Enter your guess within 1 to 10 : "))
if guess > answer: 
    print("Wrong Guess. Try smaller")
elif guess < answer: 
    print("Wrong Guess. Try bigger")
elif guess == answer:
    print("Bingo")
else:
    print("Invalid Input. Try again")    