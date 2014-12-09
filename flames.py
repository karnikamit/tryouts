#Just a Game
''' give your name and your partner's, code will give you ppl an
    appropriate result.'''
print ('*****Result is Case sensitive!*****')
game = 'FLAMESflames'
g1 = len(game)

name1 = input('your name- ') 
name2 = input("your partner's name- ")
n1 = len (name1)
n2 = len (name2)
n3 = n1 + n2
i = 0
for char in name1:
    if char in name2:
        i = i + 2

n4 = n3 - i
n5 = g1 - n4

print('\n your letter is- ',game[n5])

if game[n5]=='F' or game[n5]== 'f':
    print(' Good Friends ')
elif game[n5]== 'L' or game[n5]=='l':
    print(' Love & Love :0) ')
elif game[n5]== 'A' or game[n5]== 'a':
    print(' Affection')
elif game[n5]== 'M' or game[n5]=='m':
    print ('You\'ll get married, LoL :D')
elif game[n5]== 'E' or game[n5]== 'e':
    print(' Enemy :/')
elif game[n5]== 'S'or game[n5]=='s':
    print(' Soooper jodi')
else:
    print ('***********don\'t know*************')      
        
            
