score = int(input("Enter your score: "))

if 80 <= score <= 100:
    print("Grade: A")
elif 60 <= score  <= 79:
    print("Grade: B")
elif 50 <= score  <= 59:
    print("Grade: C")
elif 40 <= score <= 49:
    print("Grade: D")
elif 0 <= score <= 39:
    print("Grade: E")
else:
    print("Invalid entry!")
