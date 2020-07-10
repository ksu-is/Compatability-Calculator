
score_t = 0
#Have users input names
user1 = input('User 1, What is your name?: ')
user2 = input('User 2, What is your name?: ')

#Ask Questions and Record Responses
user1responses = []
user2responses = []
questions = [
    '\nQuestion 10. A) B) C) D)',
    '\nQuestion 9. A) B) C) D)',
    '\nQuestion 8. A) B) C) D)',
    '\nQuestion 7. A) B) C) D)',
    '\nQuestion 6. A) B) C) D)',
    '\nQuestion 5. A) B) C) D)',
    '\nQuestion 4. A) B) C) D)',
    '\nQuestion 3. A) B) C) D)',
    '\nQuestion 2. A) B) C) D)',
    '\nQuestion 1. A) B) C) D)'
]

def questionaire1():
    questions1 = questions
    while questions1:
        print(questions1.pop())
        user1responses.append(input('What is your answer?:'))
questionaire1()
print(user1responses)

#Repeat for second person
questions = [
    '\nQuestion 10. A) B) C) D)',
    '\nQuestion 9. A) B) C) D)',
    '\nQuestion 8. A) B) C) D)',
    '\nQuestion 7. A) B) C) D)',
    '\nQuestion 6. A) B) C) D)',
    '\nQuestion 5. A) B) C) D)',
    '\nQuestion 4. A) B) C) D)',
    '\nQuestion 3. A) B) C) D)',
    '\nQuestion 2. A) B) C) D)',
    '\nQuestion 1. A) B) C) D)'
]

def questionaire2():
    questions2 = questions
    while questions2:
        print(questions2.pop())
        user2responses.append(input('What is your answer?:'))
questionaire2()
print(user2responses)

#Compare repositories
def compcalc():
    while True:
        score_t = 0
        if user1responses[0] == user2responses[0]:
            score_t += 10
        else:
            pass
        return score_t 
compcalc()

#Return Score
print('Your Compatability Score is:', score_t,'!')
