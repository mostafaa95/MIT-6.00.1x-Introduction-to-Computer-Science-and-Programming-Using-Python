def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string

    kk = list(string.ascii_lowercase)
    for i in lettersGuessed:
        if i in kk:
            kk.remove(i)
    return "".join(kk)
