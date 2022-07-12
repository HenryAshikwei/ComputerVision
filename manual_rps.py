
from random import randint

def get_user_choice():
    user = input("Enter a choice (rock, paper, scissors): ").lower()
    
    if user == "Rock".lower():
        return user
    if user == "Paper".lower():
        return user
    if user == "Paper".lower():
        return user
    pass

def get_computer_choice():
    computer = randint(1,3)
    if computer == 1:
        computer = "Rock"
    if computer == 2:
        computer = "Paper"
    if computer == 3:
        computer = "Scissors"
    computer = computer.lower()
    return computer

def get_winner():
     
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    player_wins = 0
    computer_wins = 0
    games_played = 0

    if player_wins >= 2 and games_played == 2:
        print(f"Well done" , "You won")
    elif computer_wins == 2:
        print(f"Unlucky" , "You Lost... better luck next time!")


    if user_choice == computer_choice:
            print("You chose: " , user_choice , "and Computer chose: " , computer_choice)
            print("It's a Tie")
            print("Computer: " , computer_wins)
            print("Player: " , player_wins ) 
            pass
    
    elif user_choice == "rock":
            if computer_choice == "paper": 
                print("You lose!" , computer_choice , "covers" , user_choice)
                computer_wins += 1
                print("Computer: " , computer_wins)
                print("Player: " , player_wins ) 
            else:
                print("You win!" , user_choice , "smashes" , computer_choice)
                player_wins +=  1
                print("Computer: " , computer_wins)
                print("Player: " , player_wins ) 

                pass

    elif user_choice == "paper" :
            if computer_choice == "scissors":
                print("You lose!" , computer_choice, "cuts", user_choice)
                computer_wins += 1
                print("Computer: " , computer_wins)
                print("Player: " , player_wins )
            else: 
                print("You win!", user_choice , "covers" , computer_choice)
                player_wins += 1
                print("Computer: " , computer_wins)
                print("Player: " , player_wins ) 
                pass

            
    elif user_choice == "scissors" :
            if computer_choice == "rock" :
                print("You lose..." "Computer chose :", computer_choice , "smashes" , user_choice)
                computer_wins += 1
                print("Computer: " , computer_wins)
                print("Player: " , player_wins )
            else:
                    print("You win!.." , user_choice , "cuts" , computer_choice)
                    player_wins += 1
                    print("Computer: " , computer_wins)
                    print("Player: " , player_wins )
    games_played += 1

    if player_wins >= 2 and games_played == 2:
        print(f"Well done" , "You won")
    elif computer_wins == 2:
        print(f"Unlucky" , "You Lost... better luck next time!")
    if player_wins >= 2 and games_played == 2:
        print(f"Well done" , "You won")
    elif computer_wins == 2:
        print(f"Unlucky" , "You Lost... better luck next time!") 
    games_played += 1




def play():
    player_wins = 0
    computer_wins = 0


    name = input("Please enter your name: ")
    print("Hello!  " +  name , "Welcome to Rock, Paper, Scissors")
    print(name + ':' , player_wins ) 
    print("Computer:" , computer_wins)

    

    while True:
        get_user_choice()
        get_computer_choice()
        get_winner()




    

play()
