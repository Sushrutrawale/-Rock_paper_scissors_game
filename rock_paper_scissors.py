import random
print(" ---------------------")
print(" Rock/Paper/Scissors ")
print(" ---------------------")
listCh = ["R", "P", "S"]
name=input("ENTER YOUR GOOD NAME: ")
print("Hi!!",name,"let's play!")
playing= True

while playing:
    userScore = 0
    computerScore = 0
    round = 1
    no_of_games = int(input("Enter the no. of games you want to play: "))
    if no_of_games == 0:
        print("YOU entered 0 Game Plays!")
    while round <= no_of_games:
        computer = str(random.choice(listCh))
        print(f"Game No:[{round}]")
        user = input("Enter you choice(Press: R or P or S): ").upper()
        print("Computer's choice: ", computer)
        if user == computer:
            print("GAME IS DRAW!!")
        elif user == "R":
            
            if computer == "P":
                print(" YOU LOST!! Paper Beats Rock")
                computerScore += 1
            else:
                print("YOU WON!! Rock Beats Scissors")
                userScore += 1
        elif user == "P":
            print("Computer Enter: ", computer)
            if computer == "S":
                print("YOU LOST!! Scissors Beats Paper")
                computerScore += 1
            else:
                print("YOU WON!! Paper Beats Rock")
                userScore += 1
        elif user == "S":
            print("Computer Enter: ", computer)
            if computer == "R":
                print("YOU LOST! Rock Beats Scissors")
                computerScore += 1
            else:
                print("YOU WON! Scissors Beats Paper")
                userScore += 1
        else:
            print("SORRY!!ENTER THE CORRECT KEY")
        print("\t-------ScoreBoard-------")
        print(f"\t You: {userScore} | Computer: {computerScore}")
        print("\t--------------------------")

        round += 1
    print("\n-----GAME ENDED-----")
    print("--------------------------------")
    if userScore < computerScore:
        print("COMPUTER WON WITH SCORE:", computerScore)
        print("--------------------------------")
    elif userScore == computerScore:
        print("GAME DRAW!!")
        print("--------------------------------")
    else:
        print("YOU WON WITH SCORE:", userScore)
        print("--------------------------------")

    play_again = input("Do you want to continue(yes/no)?: ").lower()
    if not play_again == "yes":
        playing = False

        print("THANKS FOR PLAYING!!!")