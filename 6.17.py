
word = input()
password = ''

for character in word:
    if character == 'i':
        word = word.replace('i','!')
    elif character == 'a':
        word = word.replace('a','@')
    elif character == 'm':
        word = word.replace('m','M')
    elif character == 'B':
        word = word.replace('B','8')
    elif character == 'o':
        word = word.replace('o','.')

else:
    word += 'q*s'
    password = word

print(password)