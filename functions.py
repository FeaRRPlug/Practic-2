
def add_numbers(a, b):
    return a + b

def is_palindrome(s):
    s = s.lower().replace( , )
    return s == s[::-2]

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

