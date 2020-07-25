# NUMBER GUESSER

winning_number = 7

user_input =input("guess a no. b/w 1 and 10:")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN")
else:
    print("Better Luck Next Time")
