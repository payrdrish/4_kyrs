def palindrome(s):
    return s[::-1] == s
while True:
    s = input("введите слово: ")
    print(f"{s} True" if palindrome(s) else "False")

palindrome
