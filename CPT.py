def display():
    for i in range(0,len(list_one)):
        print(letter[i],list_one[i] * "*")      

letter = "ABCD"
again = "YES"
while again == "YES":         
    print("Welcome to the NIM GAME")
    print("Here are the instructions; It is a two player game, the first player and second player take turns removing any number of starts (at least one) from any pile, your goal is to take the last star to win!") 
    list_one = [5,5,5,5]
    display()

    total = 0
    while total != 1:
        user = input("Choose a line to remove stars: ")
        user = user.upper()
        while user != "A" and user !="B" and user !="C" and user !="D":
            user = input("Choose a line to remove stars: ")
        print("Next")

        user_two = int(input("How many stars do you want to remove, maximum of 5 stars: "))
        while user_two != 1 and user_two !=2 and user_two !=3 and user_two != 4 and user_two !=5:
            user_two = int(input("How many stars do you want to remove, maximum of 5 stars"))
        index = letter.find (user)
        list_one[index] = list_one[index] - user_two
        display()

        total = 0
        for x in range(0,len(list_one)):
            total += list_one[x]
            

    print("Good job you win")

    again = input("Do you want to play the game again? Enter 'YES' or 'NO': ")
    again = again.upper()
    while again != "YES" and again != "NO":
        again = input("Do you want to play the game again? Enter 'YES' or 'NO': ")

    if again == "NO":
        print("Ok Good Game!")
