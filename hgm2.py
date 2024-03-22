import random
#number of turns for one game play
turns = 7

print("Choose from the following topics: ")
n=int(input('''1.Fruits
2.Animals
3.Flowers
4.Vehicles
'''))

#vareity of topics

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
            failed += 1

#basic game mechanics

    if failed == 0:        
        print ("You won")
        break
    
    #asking user for character
    guess = input("guess a character:") 

    guesses += guess                    

    # for when guess is not found in the word
    if guess not in word:
        turns -= 1
        print ("Wrong")
        print ("You have", + turns, 'more guesses' )
 
    #Game over when turns are 0
        if turns == 0:
            print ("GAME OVER!!!")
