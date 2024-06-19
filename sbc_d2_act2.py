import random

input = input("Choose: ")


while input not in ["Kulob", "Hayang"]:
    input = input("Invalid input! Enter 'Kulob' or 'Hayang': ")

c2 = random.choice(["Kulob", "Hayang"])
c3 = random.choice(["Kulob", "Hayang"])

print(f"P1 = {input} - USER INPUT")
print(f"C2 = {c2} - RANDOM")
print(f"C3 = {c3} - RANDOM")

if input == c2 == c3:
    print("It's a tie! Maiiba!")
elif input == c2 or input == c3:
    print("P1 WINS!")
elif c2 == c3:
    print("C2 WINS!")
else:
    print("C3 WINS!")
