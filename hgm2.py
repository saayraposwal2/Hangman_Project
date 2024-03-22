import random

turns = 7

print("Choose from the following topics: ")
n=int(input('''1.Fruits
2.Animals
3.Flowers
4.Vehicles
'''))

fruits ='''Apple Banana Apricot Atemoya Avocados Blueberry Blackcurrant Ackee
Cranberry Cantaloupe Cherry Dragonfruit	Dates Cherimoya	Fig Coconut Cape gooseberry
Grapefruit Gooseberries	Sweetsop Chempedak
Hazelnut Honeyberries Durian'''.split()

animals='''Dog Kitten Cat Fish Hamster Turtle Goldfish Rabbit Mouse Puppy 
         Parrot Cow Sheep Chicken Horse Shrimp Pig Bee Crab Deer Turkey Ducks Goat Rabbit Fish Dove'''.split()

flowers='''Rose	Chrysanthemum Daisy Jasmine Gerbera Carnation Poppy Tulip Lily Lotus Hibiscus Peony
Sunflower Lilac	Aster Dandelion	Marigold Dahlia
Lamium Datura Cosmos Broom Columbine'''.split()

vehicles='''Auto Rickshaw Ambulance Aeroplane Boat Bicycle Bus Bike Car Crane Cycle
Carriage Cargo Ship Ferry Gondolas Helicopter Houseboat Jetpack Limousine Lorry Motorcycle
Metro Rowboat Ropeway Ship Scooty Scooter Tractor Train'''.split()

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
print(word)


while turns > 0:         
    failed = 0             

       
    for char in word:
        if char in guesses:
            print (char,end=""),    

        else:
            print ("_",end=""),     
            # and increase the failed counter with one
            failed += 1    

    # if failed is equal to zero

    # print You Won
    if failed == 0:        
        print ("You won")
    # exit the script
        break            
    # ask the user go guess a character
    guess = input("guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print ("Wrong")  
 
    # how many turns are left
        print ("You have", + turns, 'more guesses' )
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Lose"
            print ("You Lose"  )
