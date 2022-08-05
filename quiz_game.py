print("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay, let's play")
score = 0

answer = input("What is the capital city of Kenya? ")
if answer.lower() == "nairobi":
    print("Correct!")
    score += 1
else:
    print("wrong!, sorry:)")

answer = input("What colour is the sky? ")
if answer.lower() == "blue":
    print("Correct!")
    score += 1
else:
    print("wrong!, sorry:)")

answer = input("what's cheese made from? ")
if answer.lower() == "milk":
    print("Correct!")
    score += 1
else:
    print("wrong!, sorry:)")

answer = input("who is the king of the jungle? ")
if answer.lower() == "lion":
    print("Correct!")
    score += 1
else:
    print("wrong!, sorry:)")

answer = input("what is the sun made of? ")
if answer.lower() == "gas":
    print("Correct!")
    score += 1
else:
    print("wrong!, sorry:)")

print("you got " + str(score) + " questions correct")
print("you got " + str((score / 5) * 100) + "%.")