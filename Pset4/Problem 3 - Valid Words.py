def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    flag = True
    if word not in wordList:
        return False
    ll = hand.copy()
    for i in word:
        if ll.get(i):
            ll[i] -= 1
        else:
            flag = False
            break
    return flag
    
