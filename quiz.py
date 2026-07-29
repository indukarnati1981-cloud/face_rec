quiz= {
    "1.Who developed Python Programming Language?": "guiod van rossum",
    "2.In which year was python first released?": "1991",
    "3.What is the file extension of python files?": ".py",
    "4.Which keyword is used to define a function in python?":"class",
    "5.Which keyword is used to create a class in python?": "class",
    "6.What is the output of: len('Hello')?": "5",
    "7.Which data type is immutable: List or Tuple?": "tuple",
    "8.How do you insert comments in Python?": "#",
    "9.what will be the output of: 2 ** 3 ?": "8",
    "10.What is the output of : bool('')?": "false",
}

print("====== Welcome to python Quiz ======\n")
score = 0
# Loop through questions
for question, answer in quiz.items():
    print(question)
    user_answer = input("your answer: ").lower().strip()

    if user_answer == answer:
        print(" correct!\n")
        score += 1
    else:
        print(f" Wrong! correct answer: {answer}\n")

print("====== Quiz Completed ======")
print(f"your final score: {score}/{len(quiz)}")
# Result evaluation
if score == len(quiz):
    print(" Excellent! you're a python master!")
elif score >= 15:
    print(" Great job! solid python knowledge.")
elif score >= 10:
    print(" Good effort! keep practicing.")
else:
    print(" Needs improvement. Revise python basics!")
