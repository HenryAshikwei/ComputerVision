import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

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

user_choice = []
def get_prediction():
    highest_prob = max(prediction[0])
    if prediction [0][0] == highest_prob:
        correct_prediction = "Rock"
    elif prediction [0][1] == highest_prob:
        correct_prediction = "Paper"
    elif prediction[0][2] == highest_prob:
        correct_prediction = "Scissor"
    else:
        correct_prediction = "Nothing"
    user_choice.append(correct_prediction)
    return correct_prediction


def get_winner():
     
    user_choice = get_prediction()
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


while True: 
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)


    
    cv2.imshow('frame', frame)
    # Press q to close the window
    if prediction[0][0] > 0.7 :
        print('Rock')
    elif prediction[0][1] > 0.7:
        print('Paper')
    print(prediction)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()