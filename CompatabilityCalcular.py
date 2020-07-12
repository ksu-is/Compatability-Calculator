
score = 0
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
    score = 0
    while True:
        if user1responses[0] == user2responses [0]:
            score += 10
            continue
        elif user1responses[1] == user2responses [1]:
            score += 10
            continue
        elif user1responses[2] == user2responses [2]:
            score += 10
            continue
        elif user1responses[3] == user2responses [3]:
            score += 10
            continue
        elif user1responses[4] == user2responses [4]:
            score += 10
            continue
        elif user1responses[5] == user2responses [5]:
            score += 10
            continue
        elif user1responses[6] == user2responses [6]:
            score += 10
            continue
        elif user1responses[7] == user2responses [7]:
            score += 10
            continue
        elif user1responses[8] == user2responses [8]:
            score += 10
            continue
        elif user1responses[9] == user2responses [9]:
            score += 10
            break
        print(score)

compcalc()

#Return Score
print('Your Compatability Score is:', score_t,'!')
