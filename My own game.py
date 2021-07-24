# This is a Math game

x= 23
y= 90
print('What is your name?')
Name= input()
print('Whats up, ' + Name +'?' + ' ' + 'Want to play a multiplication game?')
one= input().lower()
if one== 'no':
    print( 'Thanks for your time, goodbye!')
elif one== 'yes':
    print(F'Alrighty then, What is {x} * {y}?')
Answer= int(input())
if Answer== 2070:
    print(F'That is correct! Great Job!!')
while Answer != 2070:
    print(F'That is incorrect, please try again.')
    Answer= int(input())

print(F'That is correct! Great Job!!')

    
    
