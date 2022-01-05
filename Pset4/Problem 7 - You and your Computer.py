def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO...
    gm = 0
    while (True):
        g = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if g == 'e':
            return
           
        elif g == 'n':
            while(True):
                p = input("Enter u to have yourself play, c to have the computer play: ")
                if p == 'u':
                    gm += 1
                    k = HAND_SIZE
                    hand = dealHand(k)
                    playHand(hand, wordList, k)
                    break
                elif p == 'c':
                    gm += 1
                    k = HAND_SIZE
                    hand = dealHand(k)
                    compPlayHand(hand, wordList, k)
                    break
                else:
                    print("Invalid command.")
                    print()
        elif g == 'r':
            if gm == 0:
                 print("You have not played a hand yet. Please play a new hand first!")
            else:
                zz = input("Enter u to have yourself play, c to have the computer play: ")
                if zz == 'u':
                    playHand(hand, wordList, k)
                elif zz == 'c':
                    compPlayHand(hand, wordList, k)
                
        else:
             print("Invalid command.")
             print()
