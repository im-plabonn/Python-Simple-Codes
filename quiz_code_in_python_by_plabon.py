name = input("Enter Your Name: ")
print(f"Hii, {name}. Welcome to the QUIZ")
playing = input("Do You Want to Play The Quiz?(Yes/No): ").lower()
if playing != "yes":
    quit()
percentage = int(input("What Percentage of Number Do You Want to Get?(10% - 100%): "))
print("Your Response Have Been Recorded")
score = 0

question1 = input("1. What is the immutable version of a list in Python? ").lower()
if question1 == "tuple":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("2. What keyword is used to define a function in Python? ").lower()
if question1 == "def":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("3. Which data type is used to store multiple values in a key-value pair format? ").lower()
if question1 == "dict":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("4. Which keyword is used to handle exceptions in Python? ").lower()
if question1 == "try":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("5. What operator is used for string concatenation? ").lower()
if question1 == "+":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("6. What is the output of 5 // 2 in Python? ").lower()
if question1 == "2":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("7. Which function is used to read input from the user? ").lower()
if question1 == "input":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("8. What keyword is used to import modules in Python?? ").lower()
if question1 == "import":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("9. Which function returns the length of a list? ").lower()
if question1 == "len":
    print("Correct")
    score += 1
else:
    print("Incorrect")

question1 = input("10. What is the built-in function to convert a string to an integer? ").lower()
if question1 == "int":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"Hii, {name}. You Got {score} Out of {10}")
per = int((score / 10) * 100)
if percentage == per:
    print(f"Congratulations 🎉🥳, {name}. You Have Fulfilled Your Target")
else:
    print(f"Sorry 😔, {name}. You Haven't Ful-fill Your Target. However, You Can Try It Again 💪.")
    print('"Never give up." — Unknown')
