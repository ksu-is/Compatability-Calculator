
score = 0
#Have users input names
user1 = input('User 1, What is your name?: ')
user2 = input('User 2, What is your name?: ')

#Ask Questions and Record Responses
user1responses = []
user2responses = []
questions = [
    '\nQuestion 10: What is your favorite movie genre? A)Horror B)Comedy C)Romance D)Action',
    '\nQuestion 9: Where do you see yourself living in 20 years? A)Near the Beach B)In the Mountains C)In the City D)In the Countryside',
    '\nQuestion 8: If you could be famous for anything, what would it be for? A)Performing (Singing/Acting/Dancing) B)Personality (TV Personality/Talk Show Host)  C)Sports D)New Invention/Discovery',
    '\nQuestion 7: If you could be a supernatural creature, which would you prefer? A)Werewolf B)Mermaid C)Vampire D)Witch',
    '\nQuestion 6: If you could have dinner with anyone, living or dead, who would it be? A)Relative B)Celebrity C)Historic Figure',
    '\nQuestion 5: Pick a talent to have? A)Singing B)Dancing C)Sports D) ',
    '\nQuestion 4: A crystal ball has appeared that can tell you about your soulmate. Would you rather know when you’ll meet, where you’ll meet, or how you’ll meet? A)When B)Where C)How',
    '\nQuestion 3: If you were able to live to the age of 90 and retain either the mind or body of a 30-year-old for the last 60 years of your life, which would you want? A)Mind B)Body',
    '\nQuestion 2: What are you most grateful for? A)Family B) C) D)',
    '\nQuestion 1: What do you think will be the most important day of your life? A)The Day You Were Born B)Wedding Day C)Tomorrow   D)Birth of First Child'
]

def questionaire1():
    questions1 = questions
    while questions1:
        print(questions1.pop())
        user1responses.append(input('What is your answer?:'))
questionaire1()

#Repeat for second person
questions = [
    '\nQuestion 10: What is your favorite movie genre? A)Horror B)Comedy C)Romance D)Action',
    '\nQuestion 9: Where do you see yourself living in 20 years? A)Near the Beach B)In the Mountains C)In the City D)In the Countryside',
    '\nQuestion 8: If you could be famous for anything, what would it be for? A)Performing (Singing/Acting/Dancing) B)Personality (TV Personality/Talk Show Host)  C)Sports D)New Invention/Discovery',
    '\nQuestion 7: If you could be a supernatural creature, which would you prefer? A)Werewolf B)Mermaid C)Vampire D)Witch',
    '\nQuestion 6: If you could have dinner with anyone, living or dead, who would it be? A)Relative B)Celebrity C)Historic Figure',
    '\nQuestion 5: Pick a talent to have? A)Singing B)Dancing C)Sports D) ',
    '\nQuestion 4: A crystal ball has appeared that can tell you about your soulmate. Would you rather know when you’ll meet, where you’ll meet, or how you’ll meet? A)When B)Where C)How',
    '\nQuestion 3: If you were able to live to the age of 90 and retain either the mind or body of a 30-year-old for the last 60 years of your life, which would you want? A)Mind B)Body',
    '\nQuestion 2: What are you most grateful for? A)Family B) C) D)',
    '\nQuestion 1: What do you think will be the most important day of your life? A)The Day You Were Born B)Wedding Day C)Tomorrow   D)Birth of First Child'
]

def questionaire2():
    questions2 = questions
    while questions2:
        print(questions2.pop())
        user2responses.append(input('What is your answer?:'))
questionaire2()

#Compare repositories
score = 0
if user1responses[0].lower() == user2responses [0].lower():
    score += 10    
if user1responses[1].lower() == user2responses [1].lower():
    score += 10
if user1responses[2].lower() == user2responses [2].lower():
    score += 10
if user1responses[3].lower() == user2responses [3].lower():
    score += 10
if user1responses[4].lower() == user2responses [4].lower():
    score += 10
if user1responses[5].lower() == user2responses [5].lower():
    score += 10
if user1responses[6].lower() == user2responses [6].lower():
    score += 10
if user1responses[7].lower() == user2responses [7].lower():
    score += 10
if user1responses[8].lower() == user2responses [8].lower():
    score += 10
if user1responses[9].lower() == user2responses [9].lower():
    score += 10
       

#Return Score
def show_results():
    x1 = (0,40)
    x2 = (50,70)
    x3 = (80,100)
    print('Your Compatability Score is:', score,'!')
    if score in x1:
        print('You and your friend don\'t seem too similar! That\'s okay, our differences make life interesting.')
    elif score in x2:
        print('You and your friend are pretty similar. Birds of a feather flock together!')
    elif score in x3:
        print('Wow! You two are really similar! They say you have 7 soulmates that you\'ll meet in life, could this be one?')
show_results()
