import random

print(("-" * 30) +"\n Rock \n Paper \n Scissors\n"+("-" * 30))
user_score, pc_score = 0,0
while True :
    print("\n1 Rock \n2 Paper \n3 Scissors ")
    user_choice= int(input("What's your choise? :"))
    pc_choice= int(random.choice(["1","2","3"]))
    if user_choice == 1:
        if pc_choice == 1:
            print("Computer's choice: Rock\nRock equal to rock. Scoreless!")
        elif pc_choice == 2:
            print("Computer's choice: Paper\nRock wraps stone. You lose!")
            pc_score += 100
        elif pc_choice == 3:    
            print("Computer's choice: Scissors\nRock breaks scissors. You win!")
            user_score +=100
    if user_choice == 2:
        if pc_choice == 1:
            print("Computer's choice: Paper\nRock wraps stone. You win!")
            user_score+=100
        elif pc_choice == 2:
            print("Computer's choice: Paper\nPaper equal to Paper. Scoreless!")
        elif pc_choice ==3:
            print ("Computer's choice:  Scissors\nPaper cuts paper. You lose!")
            pc_score +=100
    if user_choice ==3:
        if pc_choice == 1 :
            print("Computer's choice: Rock\nScissors breaks scissors. You lose!")
            pc_score +=100
        elif pc_choice == 2 :
            print("Computer's choice: Paper\nScissors cuts paper. You Win!")
            user_score+=100
        elif pc_choice == 3 :
            print("Computer's choice: Scissors\nScissors equal to Scissors. Scoreless!")
    print("\nUser's score: {}\nComputer's score: {}".format(user_score, pc_score))

