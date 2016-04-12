
# coding: utf-8

# # Dice Roll Simulator

# In[2]:

from random import randint


# In[3]:

def dice_roll():
    print randint(1,6)
    ans = raw_input("Would you like to roll again? (y/n) \n")
    while True:
        if ans.lower()=="y":
            return dice_roll()
        elif ans.lower()=="n":
            return "Thanks for playing!"
        else:
            print "Sorry, I didn't get that, please type your answer again."
            ans = raw_input("Would you like to roll again? (y/n) \n")


# In[4]:

dice_roll()


# In[ ]:

# Guess The Number


# In[5]:

def guess_int():
    target = randint(0,100)
    while True:
        guess = raw_input("Guess an integer between 0 and 100! \n")
        if int(guess) == target:
            return "Correct! You win!"
        elif int(guess) < target:
            print "You need to go higher..."
            more = raw_input("Would you like to take another guess? (y/n) \n")
            while more.lower() != "y":
                if more.lower()=="n":
                    return "Thanks for playing!"
                else:
                    print "Sorry, I didn't get that, please type your answer again."
                    more = raw_input("Would you like to take another guess? (y/n) \n")
        elif int(guess) > target:
            print "You need to go lower..."
            more = raw_input("Would you like to take another guess? (y/n) \n")
            while more.lower() != "y":
                if more.lower()=="n":
                    return "Thanks for playing!"
                else:
                    print "Sorry, I didn't get that, please type your answer again."
                    more = raw_input("Would you like to take another guess? (y/n) \n")
        else:
            return "You must enter an integer!"


# In[6]:

guess_int()


# # Mad Libs Generator

# In[7]:

def mad_libs():
    story_prior_noun = "Once upon a time, there was a young "
    story_post_noun = " named "
    story_prior_adj = " who really loved dancing, pringles, trains and really "
    story_post_adj = " penguins. "
    story_prior_verb = "'s favourite activity to do along whith dancing, and often at the same time, is "
    story_post_verb = " and can do it all day long. The End."
    
    noun_a = raw_input("Please enter a type of object (animal/person): ")
    noun_b = raw_input("Please enter a name: ")
    adj = raw_input("Please enter an adjective: ")
    verb = raw_input("Please enter a verb: ")
    
    return story_prior_noun+noun_a+story_post_noun+noun_b+story_prior_adj+adj+story_post_adj+noun_b+story_prior_verb+verb+story_post_verb


# In[8]:

mad_libs()


# # Hangman

# In[9]:

word_list = ['time', 
'year', 
'people', 
'way', 
'day', 
'man', 
'thing', 
'woman', 
'life', 
'child', 
'world', 
'school', 
'state', 
'family', 
'student', 
'group', 
'country', 
'problem', 
'hand', 
'part', 
'place', 
'case', 
'week', 
'company', 
'system', 
'program', 
'question', 
'work', 
'government', 
'number', 
'night', 
'point', 
'home', 
'water', 
'room', 
'mother', 
'area', 
'money', 
'story', 
'fact', 
'month', 
'lot', 
'right', 
'study', 
'book', 
'eye', 
'job', 
'word', 
'business', 
'issue', 
'side', 
'kind', 
'head', 
'house', 
'service', 
'friend', 
'father', 
'power', 
'hour', 
'game', 
'line', 
'end', 
'member', 
'law', 
'car', 
'city', 
'community', 
'name', 
'president', 
'team', 
'minute', 
'idea', 
'kid', 
'body', 
'information', 
'back', 
'parent', 
'face', 
'others', 
'level', 
'office', 
'door', 
'health', 
'person', 
'art', 
'war', 
'history', 
'party', 
'result', 
'change', 
'morning', 
'reason', 
'research', 
'girl', 
'guy', 
'moment', 
'air', 
'teacher', 
'force', 
'education', 
]

def hangman():
    word = word_list[randint(1,100)]
    board = ['_']*len(word)
    print board
    goes = 0
    while goes < 8:
        guess = raw_input("Guess a letter! \n")
        if len(guess) !=1 or not guess.isalpha():
            print " you must enter just one alphabetical letter!"
        else:
            indexes=[]
            for index, letter in enumerate(word):
                if guess == letter:
                    indexes.append(index)
            for item in indexes:
                board[item]=guess
            print board
            attempt = raw_input("Take a guess at the word! \n")
            if attempt == word:
                return "Yes, the answer is %s! You win!" % word
            else:
                print "Sorry, that's not right."
            goes = goes + 1
    attempt = raw_input("You've run out of goes. Take a guess at the word! \n")
    if attempt == word:
        return "Yes, the answer is %.! You win!" % word
    else:
        return "Sorry, that's not right, the word was %s. You lose!" % word


# In[10]:

hangman()


# # Textbased Adventure Game

# In[ ]:

"""The Goal: Remember Adventure? Well, we’re going to build a more basic version of that. A complete text game, the program will
let users move through rooms based on user input and get descriptions of each room. To create this, you’ll need to establish the
directions in which the user can move, a way to track how far the user has moved (and therefore which room he/she is in), and to
print out a description. You’ll also need to set limits for how far the user can move. In other words, create “walls” around the
rooms that tell the user, 'You can’t move further in this direction.' """


# In[11]:

#imagine a 2x3 grid
#bedroom1 bathroom bedroom2
#livingRoom Porch Kitchen
#index this with coordinates [1,1] to [2,3]
#All users start in the porch, which leads to either the living room or kitchen or bathroom
#both bedrooms lead to the bathroom
#the livingroom leads to bedroom1 and the kitchen leads to bedroom2

def ad_house():
    house_desc = {"Living room": " has a tv and a grey sofa", "Porch":" has a shoe rack and an ottoman",
                  "Kitchen":" has grey work-tops and white units", "Bathroom":" has beige stone walls and a bath with a shower",
                 "First Bedroom": " has a double bed", "Second Bedroom": " has a kingsize bed", "The outside":"You left the house."}
    house_plan = {"[1,1]":"Living room", "[1,2]":"Porch", "[1,3]":"Kitchen","[2,1]":"First Bedroom", "[2,2]":"Bathroom",
                  "[2,3]":"Second Bedroom", "[0,2]":"The outside"}
    position = [1,2]
    while True:
        print "The "+house_plan["["+str(position[0])+","+str(position[1])+"]"]+house_desc[house_plan["["+str(position[0])+","+str(position[1])+"]"]]
        escape = raw_input("If you must leave now, please type 'Beam me up Scottie'. To stay enter anything else. \n")
        if escape.lower() == "beam me up scottie":
            return "Beaming you up. Good bye!"
        else:
            print "Let's keep exploring!"
        step = raw_input("Enter your step direction (f/b/l/r) \n")
        if step.lower() == "f":
            if position[0] == 2:
                print "You can't move in this direction, please choose a different step."
            else:
                position[0] = position[0]+1
        elif step.lower() == "b":
            if (position[0]==1 and position[1] != 2):
                print "You can't move in this direction, please choose a different step."
            else:
                position[0] = position[0]-1
                if position == [0,2]:
                    print house_desc[house_plan["[0,2]"]]
                    return "Leaving the house ends the game. Good bye."
        elif step.lower() == "l":
            if position[1]==1:
                print "You can't move in this direction, please choose a different step."
            else:
                position[1] = position[1]-1
        elif step.lower() == "r":
            if position[1]==3:
                print "You can't move in this direction, please choose a different step."
            else:
                position[1] = position[1]+1
        else:
            print "You entered something which isn't a valid step. Please enter f/b/l/r."


# In[12]:

ad_house()

