import random
from art import logo
from art import vs
from game_data import data
import os

point = 0
game_over = False

def dataname(datas):  
    country1 = datas["country"]    
    name1 = datas["name"]    
    job1 = datas["description"]
    return f"{name1}, a {job1}, from {country1}"
    
def check(guess,folower1,folower2):
    if folower1 > folower2:
        return guess == "a"
    else:
        return guess == "b"

choice2 = random.choice(data)
while not game_over:
    choice1 = choice2
    choice2 = random.choice(data)

    if choice1 == choice2:
        choice2 = random.choice(data)
    
        
    print(logo)
    print(f"Compare A: {dataname(choice1)}")
    
    print(vs)
    print(f"Compare B: {dataname(choice2)}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
         
    folower1 = choice1["follower_count"]
    folower2 = choice2["follower_count"]   
    benar = check(guess,folower1,folower2)

    os.system('cls')
    print(logo)
    if benar:
        point += 15
        print(f"You got it right! Your point is: {point}")
    else:
        
        game_over = True
        print(f"Sorry, you got it Wrong! Your point is: {point}")
        
    