cat = 'My cat, Lola, is black.'

# Using only sequence access and slicing, extract 
# values from the string above to produce the expected outputs shown 
# below.

# An example:
# Expected output: '.'
print(cat[-1])

# Expected output: 'b'
print(cat[-6])

# Expected output: 'Lola'
print(cat[8:12:1])

# Expected output: 'yct oa sbak'
print(cat[1::2])

# Expected output: 'kcalb'
print(cat[-2:-7:-1])

# Expected output: 'My cat, Lola, is black.'
print(cat[::])
# You can't just use print(cat) here. You must use indexing/slicing.
