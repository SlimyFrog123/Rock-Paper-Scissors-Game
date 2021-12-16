import random

global winner

winner = "na"

def main():
    global winner
    choice = int(input("Which symbol would you like to be? (1: rock, 2: paper, 3: scissors)"))
    generated_choice = random.randint(1, 3) #1: rock, 2: paper, 3: scissors
    #Choice1
    #Choice2
    if choice == 1:
        Choice1 = "Rock"
    elif choice == 2:
        Choice1 = "Paper"
    elif choice == 3:
        Choice1 = "Scissors"
    
    if generated_choice == 1:
        Choice2 = "Rock"
    elif generated_choice == 2:
        Choice2 = "Paper"
    elif generated_choice == 3:
        Choice2 = "Scissors"
    
    
    #Logic (who won?):
    if choice == 1 and generated_choice == 2:
        winner = "AI"
    elif choice == 2 and generated_choice == 2:
        winner = "na"
    elif choice == 3 and generated_choice == 2:
        winner = "You"
    elif choice == 1 and generated_choice == 1:
        winner = "na"
    elif choice == 2 and generated_choice == 1:
        winner = "You"
    elif choice == 3 and generated_choice == 1:
        winner = "AI"
    elif choice == 1 and generated_choice == 3:
        winner = "You"
    elif choice == 2 and generated_choice == 3:
        winner = "AI"
    elif choice == 3 and generated_choice == 3:
        winner = "You"
    
    print("You chose " + Choice1 + ", and the AI chose " + Choice2)
    print(winner + " won")

if __name__ == "__main__":
    main()
