import random
print("🎮 Number Guessing Game")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-500)")

choice = input("Choose difficulty (1/2/3): ")

if choice == "1":
    max_num = 50
elif choice == "2":
    max_num = 100
else:
    max_num = 500

secret_number = random.randint(1, max_num)
attempts = 0

while True:
    guess = int(input(f"Guess a number between 1 and {max_num}: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"🎉 You won in {attempts} attempts!")
        break