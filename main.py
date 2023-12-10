from helpers import set_board, check_turn, check_for_wins, choose_starting_player, choose_marks
import os

#Boat setting
spots = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

playing = True
complete = False
turn = 0
prev_turn = -1

name1 = input("Players 1 nickname: ")
name2 = input("Players 2 nickname: ")
starting_player = choose_starting_player(name1, name2)

if starting_player == name1:
  other_player = name2
else:
  other_player = name1

mark1, mark2 = choose_marks(starting_player)

while playing:
  #Reset the screen
  os.system('cls' if os.name == "nt" else "clear")
  set_board(spots)

  #Check the input 
  if prev_turn == turn:
    #Error of the input is not digit
    if choice.isdigit() == False and choice != "q":
      print("The input should be digit. Let's try again.")

    #Error if the input number is not 1-9
    elif int(choice) < 1 or int(choice) > 9 and choice != "q":
      print("The number should be from 1 to 9. Let's try again.")

    #Check if X/0 is already in the spot or not
    elif spots[int(choice)] in {"X", "0"}:
      print("The mark is already in the spot. Let's try again.")
  
  prev_turn = turn

  if turn % 2 == 0:
    print(starting_player + " turn. Please select the number of the spot.")
    print("Print q to quit\n")
  else:
    print(other_player + " turn. Please select the number of the spot.")
    print("Print q to quit\n")
  
  #Input from the player
  choice = input()

  #Quitting the game
  if choice == "q":
    playing = False
    print("You quit the game")

  #If the input contains digits only and not in the "occupied" spot than OK - continue:
  elif choice.isdigit() and int(choice) in spots:
    if not spots[int(choice)] in {"X", "0"}:
      turn += 1
      spots[int(choice)] = check_turn(turn, mark1, mark2)
      
  #Check if the game has ended:
  if check_for_wins(spots):
    playing = False
    complete = True

  #Tie
  if turn > 8: 
    playing = False

#Drawing the board for the last time
os.system('cls' if os.name == "nt" else "clear")
set_board(spots)

#Game results
if complete:
  if check_turn(turn, mark1, mark2) == mark1:
    print(starting_player + " won")
  else:
    print(other_player + " won")
else:
  print("No winner")

print("Thank you for playing <3")
    
