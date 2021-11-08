# You have been given two lists containing some of our favourite 
# programming languages. Use the append, extend & remove list methods
# to produce a list you will print() to display the expected output.

prog_lang_one = ['C#', 'JavaScript', 'Kotlin', 'Python']
prog_lang_two = ['C++', 'Go', 'Java', 'Swift']

# Write your solution here
prog_lang_one.append('TypeScript')
prog_lang_two.remove('Swift')
prog_lang_one.append(prog_lang_two)

print(prog_lang_one)
# Expected output:
# ['C#', 'JavaScript', 'Kotlin', 'Python', 'TypeScript', 'C++', 'Go', 'Java']

