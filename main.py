answer = input("Enter your answer: ")
correct_answer = input("Enter the correct one: ")
if answer == correct_answer:
    print("you are the winner")
if answer != correct_answer:
    print("2 attempts left")
answer = input("Enter your answer: ")
if answer != correct_answer:
    print("1 attempt left")
if answer == correct_answer:
    print("you are the winner")
answer = input("Enter your answer: ")
if answer != correct_answer:
    print("failed")
if answer == correct_answer:
    print("you are the winner")