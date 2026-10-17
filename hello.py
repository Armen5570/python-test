# # 1
# number = [10,20,30,40,50]
# number.reverse()
# print(number)
# # 2
# numbers = [10, 30, 20, 40]
# numbers.reverse()

# print(numbers)
# # 3
# numbers = [50, 10, 40, 20, 30]
# numbers.sort(reverse=True)

# print(numbers)

# # 4
# numbers = [10, 20, 30, 40]
# numbers.pop()

# print(numbers)
# # 5
# fruits = ["apple", "banana", "orange"]
# fruits.remove("banana")

# print(fruits)

# # 6

# fruits = ["apple", "banana"]
# fruits.append("orange")

# print(fruits)

# # 7

# fruits = ["apple", "banana", "orange"]
# print(fruits)

# # 8
# text = "   Hello   "
# print(text.strip())

# # 9
# text = "I like Java"
# print(text.replace("Java", "Python"))

# # 10
# text = "hello world armen"
# print(text.title())

# # 11
# text = "hELLO WORLD"
# print(text.capitalize())

# # 12
# text = "HELLO PYTHON"
# print(text.lower())

# # 13
# name = "Armen"
# print(name.upper())


import random

number = random.randint(1, 100)
attempts = 0

print("================================")
print("    NUMBER GUESSING GAME")
print("================================")
print("I picked a number from 1 to 100!")
print("Can you guess it?")
print("Type '0' to quit.")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if guess == 0:
        print("Game over! See you next time.")
        break

    if guess < 1 or guess > 100:
        print("Choose a number between 1 and 100!")
        continue

    attempts += 1

    if guess < number:
        print("Too low! Try a higher number.")
    elif guess > number:
        print("Too high! Try a lower number.")
    else:
        print(f"\n🎉 Correct! The number was {number}!")
        print(f"You won in {attempts} attempts!")
        break

print("Thanks for playing!")
