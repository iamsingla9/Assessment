def calculate_palindrome(word):
    n = len(word)
    half = n//2
    for i in range(half+1):
        if(word[i] != word[n -i -1]):
            return(0)
    return(1)
   
if __name__ == '__main__':
    word = str(input().rstrip())
    result = calculate_palindrome(word.lower())
    if(result):
        print("Yes, the input is a plindrome.")
    else:
        print("No, the input is not a palindrome.")