#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.
import random
import time
import sys

def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will be playing against the computer.")
    print("The first to 3 points wins!")
    print("Good luck!")

    #variables
    playerScore = 0
    computerScore = 0
    rounds = 0
    options = ["rock", "paper", "scissors"]
    
    #game loop
    
    while playerScore < 3 and computerScore < 3:
        print("Round " + str(rounds + 1))
        playerChoice = input("Please choose rock, paper, or scissors: ")
        playerChoice = playerChoice.lower()
        if playerChoice in options:
            computerChoice = random.choice(options)
            print("The computer chose " + computerChoice)
            if playerChoice == "rock" and computerChoice == "scissors":
                print("You win!")
                playerScore += 1
            elif playerChoice == "paper" and computerChoice == "rock":
                print("You win!")
                playerScore += 1
            elif playerChoice == "scissors" and computerChoice == "paper":
                print("You win!")
                playerScore += 1
            elif playerChoice == computerChoice:
                print("It's a tie!")
            else:
                print("You lose!")
                computerScore += 1
            rounds += 1
        else:
            print("Invalid option. Please try again.")
    if playerScore == 3:
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose.")
    print("Final Score: Player: " + str(playerScore) + " Computer: " + str(computerScore))
    playAgain = input("Would you like to play again? (y/n): ")
    playAgain = playAgain.lower()
    if playAgain == "y":
        main()
    else:
        print("Thanks for playing!")
        time.sleep(2)
        sys.exit()
main()


    




