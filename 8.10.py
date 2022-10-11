word = str(input())
word = word
new_word = word.replace("","")
new = new_word[::1]

if new_word == new:
    print('{} is a palindrome'.format(word))
else:
    print('{} is not a palindrome'.format(word))
