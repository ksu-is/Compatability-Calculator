
score = 0
#Have users input names
user1 = input('User 1, What is your name?: ')
user2 = input('User 2, What is your name?: ')

#Ask Questions and Record Responses
user1responses = []
user2responses = []
questions = [
    '\nQuestion 10: What is your favorite movie genre? \nA )Horror \nB) Comedy \nC) Romance \nD) Action',
    '\nQuestion 9: Where do you see yourself living in 20 years? \nA) Near the Beach \nB) In the Mountains \nC) In a Major City \nD) In the Countryside',
    '\nQuestion 8: If you could be famous for anything, what would it be for? \nA) Performing (Singing/Acting/Dancing) \nB) Your Personality (TV Personality/Talk Show Host/Influencer)  \nC) Sports \nD) New Invention/Discovery',
    '\nQuestion 7: If you could be a supernatural creature, which would you want to be? \nA) Werewolf \nB )Mermaid \nC) Vampire \nD) Witch',
    '\nQuestion 6: If you could have dinner tonight with anyone, living or dead, who would it be with? \nA) A Relative \n B) A Celebrity \n C) A Historic Figure',
    '\nQuestion 5: Pick something to be an expert at: \nA) An Instrument \nB) A Sport \nC) Debates \nD) Performance (Singing/Acting/Dancing)',
    '\nQuestion 4: A crystal ball has appeared that can tell you one specific thing about your soulmate. Would you rather know... \nA) When you’ll meet \nB) Where you’ll meet \nC) How you’ll meet?',
    '\nQuestion 3: If you were able to live to the age of 90 and retain either the mind or body of a 30-year-old for the last 60 years of your life, which would you want? \nA)Mind \nB)Body',
    '\nQuestion 2: Pick a Quote. \nA) "The Choice you refuse to make is the choice that will be made for you" \nB) "Success requires no apologies. Failure permits no alibis." \nC) "If you\'re going through hell...keep going." \nD) "You only live once, but if you do it right, once is enough."',
    '\nQuestion 1: What do you think is the most important day in your life? \nA) The day you were born \nB) Your Wedding Day \nC) Tomorrow   \nD) The birth of your first child'
]
print(user1, 'please answer the following questions...')
def questionaire1():
    questions1 = questions
    while questions1:
        print(questions1.pop())
        user1responses.append(input('Please select an answer:'))
questionaire1()

#Repeat for second person
questions = [
    '\nQuestion 10: What is your favorite movie genre? \nA)Horror \nB) Comedy \nC) Romance \nD) Action',
    '\nQuestion 9: Where do you see yourself living in 20 years? \nA) Near the Beach \nB) In the Mountains \nC) In a Major City \nD) In the Countryside',
    '\nQuestion 8: If you could be famous for anything, what would it be for? \nA) Performing (Singing/Acting/Dancing) \nB) Your Personality (TV Personality/Talk Show Host/Influencer)  \nC) Sports \nD) New Invention/Discovery',
    '\nQuestion 7: If you could be a supernatural creature, which would you want to be? \nA) Werewolf \nB)Mermaid \nC) Vampire \nD) Witch',
    '\nQuestion 6: If you could have dinner tonight with anyone, living or dead, who would it be with? \nA) A Relative \nB) A Celebrity \nC) A Historic Figure',
    '\nQuestion 5: Pick something to be an expert at: \nA) An Instrument \nB) A Sport \nC) Debates/Talking to People \nD) Performance (Singing/Acting/Dancing)',
    '\nQuestion 4: A crystal ball has appeared that can tell you one specific thing about your soulmate. Would you rather know... \nA) When you’ll meet \nB) Where you’ll meet \nC) How you’ll meet?',
    '\nQuestion 3: If you were able to live to the age of 90 and retain either the mind or body of a 30-year-old for the last 60 years of your life, which would you want? \nA)Mind \nB)Body',
    '\nQuestion 2: Pick a Quote. \nA) "The Choice you refuse to make is the choice that will be made for you" \nB) "Success requires no apologies. Failure permits no alibis." \nC) "If you\'re going through hell....keep..going.." \nD) "You only live once, but if you do it right, once is enough."',
    '\nQuestion 1: What do you think is the most important day in someone\'s life? \nA) The day you\'re born \nB) Your Wedding Day \nC) Your Last   \nD) The birth of your first child'
]

print(user2, 'please answer the following questions...')
def questionaire2():
    questions2 = questions
    while questions2:
        print(questions2.pop())
        user2responses.append(input('User 2, please select an answer:'))
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
    print(f'{user1}...{user2}...Your Compatability Score is:', score,'!')
    if score in x1:
        print('You and your friend don\'t seem too similar! That\'s okay, our differences make life interesting.')
    elif score in x2:
        print('You and your friend are pretty similar. Birds of a feather flock together!')
    elif score in x3:
        print('Wow! You two are really similar! They everyone has 7 soulmates in life, could this be one?')
show_results()

