import random
c="y"
while c in "yY":
    #number of turns for one game play
    turns = 7

    print("Choose from the following topics: ")
    n=int(input('''1.Fruits
2.Animals
3.Flowers
4.Vehicles
'''))

    #vareity of topics

    fruits ='''apple banana apricot atemoya avocados blueberry blackcurrant ackee cranberry cantaloupe cherry dragonfruit dates cherimoya fig coconut cape gooseberry grapefruit sweetsop chempedak hazelnut honeyberries durian'''.split()

    animals='''dog kitten cat fish hamster turtle goldfish rabbit mouse puppy parrot cow sheep chicken horse shrimp pig bee crab deer turkey ducks goat rabbit fish dove'''.split()

    flowers='''rose chrysanthemum daisy jasmine gerbera carnation poppy tulip lily lotus hibiscus peony sunflower lilac aster dandelion marigold dahlia lamium datura cosmos broom columbine'''.split()

    vehicles='''auto rickshaw ambulance aeroplane boat bicycle bus bike car crane cycle carriage cargo ship ferry gondolas helicopter houseboat jetpack limousine lorry motorcycle metro rowboat ropeway ship scooty tractor train'''.split()

    if(n==1):
        t=random.randint(0,len(fruits)-1)
        word = fruits[t]
    elif(n==2):
        t=random.randint(0,len(animals)-1)
        word = animals[t]
    elif(n==3):
        t=random.randint(0,len(flowers)-1)
        word = flowers[t]
    elif(n==4):
        t=random.randint(0,len(vehicles)-1)
        word = vehicles[t]
    
    else:
        print("invalid input")
    
    guesses = ''



    while turns > 0:         
        failed = 0             

       
        for char in word:
            if char in guesses:
                print (char,end=""),    

            else:
                print ("_",end=""),     
                failed += 1

    #basic game mechanics

        if failed == 0:        
            print ("You won")
            break
    
        #asking user for character
        guess = input("  guess a character:") 

        guesses += guess                    

        # for when guess is not found in the word
        if guess not in word:
            turns -= 1
            print ("Wrong")
            print ("You have",turns, 'more guesses' )
 
        #Game over when turns are 0
            if turns == 0:
                print("The word was:",word)
                print ("GAME OVER!!!")
                
    c=input("Play Again? Y/N")
print("Thank You For Playing!!!")
