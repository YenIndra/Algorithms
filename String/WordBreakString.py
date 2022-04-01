def wordBreak(line, dictionary):
    # Complete this function
    if line == '':
        return True
    else:
        wordLen = len(line)
        return any([(line[:i] in dictionary) and wordBreak(line[i:], dictionary) for i in range(1, wordLen+1)])
