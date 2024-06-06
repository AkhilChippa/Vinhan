def is_palindrome(s: str) -> bool:
    reverse_s=s[::-1]
    if reverse_s==s:
        return "True"
    else:
        return "False"
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False