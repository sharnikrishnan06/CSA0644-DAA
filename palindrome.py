def firstPalindrome(words):
    for w in words:
        if w == w[::-1]:
            return w
    return ""

words = ["abc","car","ada","racecar","cool"]
print(firstPalindrome(words))
