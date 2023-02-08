def palindrome(word):
    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        return palindrome(word[1: -1])
    else:
        return False


print(palindrome('camera'))
