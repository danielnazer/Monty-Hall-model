#modeling the monty hall problem

import random
#simulate not changing doors
#player sticks with first choice regardless of what goat door Monty Hall opens
correct_guesses_stick = int(0)
incorrect_guesses_stick = int(0)
for i in range (0, 1000000):
    first_choice = random.choice(["A", "B", "C"])
    door_with_car_behind_it = random.choice(["A", "B", "C"])
    first_randomly_chosen_goat_door = door_with_car_behind_it 
    second_randomly_chosen_goat_door = door_with_car_behind_it 
    while first_randomly_chosen_goat_door == door_with_car_behind_it:
        first_randomly_chosen_goat_door = random.choice(["A", "B", "C"])  
    while second_randomly_chosen_goat_door == door_with_car_behind_it or second_randomly_chosen_goat_door == first_randomly_chosen_goat_door:
        second_randomly_chosen_goat_door = random.choice(["A", "B", "C"])
    if first_choice == door_with_car_behind_it:
        correct_guesses_stick = correct_guesses_stick + 1
    if first_choice != door_with_car_behind_it:
        incorrect_guesses_stick = incorrect_guesses_stick + 1
#simulate_changing doors
#If player selects the door with the car, then Monty Hall will open the first randomly chosen goat door and the player will switch selection to the second randomly chosen goat door
#If player chooses a goat door, Monty Hall opens other goat door. Player then switches to the car door        
correct_guesses_switch = int(0)
incorrect_guesses_switch = int(0)
for i in range (0, 1000000):
    door_with_car_behind_it = random.choice(["A", "B", "C"])
    first_randomly_chosen_goat_door = door_with_car_behind_it 
    second_randomly_chosen_goat_door = door_with_car_behind_it 
    while first_randomly_chosen_goat_door == door_with_car_behind_it:
        first_randomly_chosen_goat_door = random.choice(["A", "B", "C"])  
    while second_randomly_chosen_goat_door == door_with_car_behind_it or second_randomly_chosen_goat_door == first_randomly_chosen_goat_door:
        second_randomly_chosen_goat_door = random.choice(["A", "B", "C"])
    first_choice = random.choice(["A", "B", "C"])
    if first_choice == door_with_car_behind_it:
        second_choice = second_randomly_chosen_goat_door
        incorrect_guesses_switch = incorrect_guesses_switch + 1
    if first_choice != door_with_car_behind_it:
        second_choice = door_with_car_behind_it
        correct_guesses_switch = correct_guesses_switch + 1
#print out results of simulation
print "Out of 1,000,000 players who stuck with their first guess,", correct_guesses_stick, "won a car."
print "Out of 1,000,000 players who stuck with their first guess,", incorrect_guesses_stick, "won a goat."
print "Out of 1,000,000 players who switched doors,", correct_guesses_switch, "won a car."
print "Out of 1,000,000 players who switched doors,", incorrect_guesses_switch, "won a goat."
