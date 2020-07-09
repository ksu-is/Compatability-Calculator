Score = 0
#Have users input names
user1 = input('User 1, What is your name?: ')
user2 = input('User 2, What is your name?: ')

#Ask Questions and Record Responses
user1responses = []
user2responses = []
questions = [
    'Question 1. A) B) C) D)\n'
    'Question 2. A) B) C) D)\n'
    'Question 3. A) B) C) D)\n'
    'Question 4. A) B) C) D)\n'
    'Question 5. A) B) C) D)\n'
    'Question 6. A) B) C) D)\n'
    'Question 7. A) B) C) D)\n'
    'Question 8. A) B) C) D)\n'
    'Question 9. A) B) C) D)\n'
    'Question 10. A) B) C) D)\n'
]
def questionnaire1():
    questions1 = questions
    for question in questions1:
        asking = questions1.pop()
        print(asking)
        user1responses.append = input('What is your answer?:')
questionnaire1()

#Repeat for second person
def questionnaire2():
    questions2 = questions
    while question in questions2:
        asking = questions2.pop()
        print(asking)
        user2responses.append = input()
questionnaire2()

#Compare repositories
while True:
    if user1responses[0] == user2responses [0]:
        Score += 10
        user1responses.pop(0)
        user2responses.pop(0)
   
#Return Score
print("Your Compatability Score is:", Score + '!')