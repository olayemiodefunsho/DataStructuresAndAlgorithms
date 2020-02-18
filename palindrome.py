# O(n^2) time | O(n) space
# def isPalindrome(string):
#     reversedString = ""
#     for i in reversed(range(len(string))):
#         reversedString += string[i]
#     return string == reversedString

# O(n) time | O(n) space
def isPalindrome(string):
    reversedChars = []
    for i in reversed(range(len(string))):
        reversedChars.append(string[i]) 
    return string == "".join(string[i])
