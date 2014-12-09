import random
cases = int(input('cases:' ))
for case in range(cases):
        
    movie_list = {1: 'Rangeela', 2: 'Dhoom', 3: 'Raanjhana', 4: 'Devdas'}
    name = movie_list[random.randint(1, 4)]

    a  = len(name)


    print (" This movie name has ", a, 'letters')
    print (name[0], '*'* (a-2), name[a-1])

    q = input('Guess the name of the bollywood movie - ')

    i = 0
    while i < a:
       
        
        for char in name[i]:
            if char in q[i]:
                print(char)
                
            else:
                print('XXX- better luck next time!')
                
            i = i + 1
    if name == q:
        print("Congratulations!")
    else:
        print("next time buddy")

    input()
