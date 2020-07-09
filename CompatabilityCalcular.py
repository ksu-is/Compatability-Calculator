Score = 0
#Have users input names
user1 = input('User 1, What is your name?: ')
user2 = input('User 2, What is your name?: ')

#Ask Questions and Record Responses
user1responses = []
user2responses = []
questions = [
    '\nQuestion 1. A) B) C) D)',
    'Question 2. A) B) C) D)',
    'Question 3. A) B) C) D)',
    'Question 4. A) B) C) D)',
    'Question 5. A) B) C) D)',
    'Question 6. A) B) C) D)',
    'Question 7. A) B) C) D)',
    'Question 8. A) B) C) D)',
    'Question 9. A) B) C) D)',
    'Question 10. A) B) C) D)'
]
def questionaire1():
    questions1 = questions
    while questions1:
        print(questions1.pop())
        user1responses.append(input('What is your answer?:'))
questionaire1()
print(user1responses)

#Repeat for second person
def questionaire2():
    questions2 = questions
    while questions2:
        print(questions2.pop())
        user2responses.append(input('What is your answer?:'))
questionaire2()
print(user2responses)

#Compare repositories
while True:
    if user1responses[0] == user2responses [0]:
        Score += 10
        user1responses.pop(0)
        user2responses.pop(0)
   
#Return Score
print("Your Compatability Score is:", Score + '!')