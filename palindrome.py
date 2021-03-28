def is_palindrome(s):
    """
    Non-letters and capitalization are ignored
    :param s: str
    :return: True if letters in s form a palindrome; False otherwise
    """

    def to_chars(s):
        s = s.lower()
        letters = ''
        for char in s:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                letters += char
        return letters

    def is_pal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and is_pal(s[1:-1])

    return is_pal(to_chars(s))

s = 'racecar'
print(is_palindrome(s))