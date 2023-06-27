topic = input("What is my name?")
answer = input("Enter your answer: ")
correct_answer = input("Enter the correct one: ")
if answer == correct_answer:
    print("you are the winner")
if answer != correct_answer:
    print("2 attempts left")
    pass
answer = input("Enter your answer: ")
if answer != correct_answer:
    print("1 attempt left")
    pass
answer = input("Enter your answer: ")
if answer != correct_answer:
    print("failed")
