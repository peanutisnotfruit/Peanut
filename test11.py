import random
coin_result = random.randint(1,2)

choice = int(input("Enter your choice (head for 1/tail for 2) : "))

if choice == 1 and coin_result == 1:
    print("It's Head. You won")
elif choice == 1 and coin_result == 2:
    print("It's tail. You loose")
elif choice == 2 and coin_result == 2:
    print("It's tail> You won")
elif choice == 2 and coin_result == 1:
    print("It's head you lose")