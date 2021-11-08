# The code below raise an exception. Why? Modify the code to use a
# try/except block to handle it.

try:
    with open('foo.txt') as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}")
else:
    print(data)


# Why does this code raise an exception? Answer below.
# if foo.txt doesn't exist or can't be found it then raises an error