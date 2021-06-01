import random

gamelist = ['rock', 'paper', 'scissors']

def game(comp,player):
    if(comp==player):
        return None
    if(comp=='rock'): 
        if(player=='scissors'):
            return True
        else:
            return False
    if(comp=='paper'):
        if(player=='scissors'):
            return True
        else:
            return False
    if(comp=='scissors'):
        if(player=='paper'):
            return True
        else:
            return False

    

print('''
\t Game
write any one of the following:-
- rock
- paper 
- scissors
''')

comp=print("Computer's Turn")
comp=random.choice(gamelist)
player=input("Your Turn: ")

print(f"\nComputer's choice: {comp}")
print(f"Yourchoice: {player}")

a = game(comp,player)
if(a==None):
    
    print("\nIT'S A TIE!!")
elif(a):
   
    print("\nComputer Won!! [better luck next time]")
else:
    
    print("\nCongrats!! You Won!!")




