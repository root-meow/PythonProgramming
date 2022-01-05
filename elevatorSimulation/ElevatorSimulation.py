#Import
import time #for creating delay.


# initialize variables.
max_floor = 4
min_floor = 0
ground_floor = 0
first_floor = 1
second_floor = 2
third_floor = 3
fourth_floor = 4
destination_floor = None


# create list to hold values when elevator is going up or down.
going_up = []
going_down = []

#Incase there are different passengers

"""def invalid_input(int):
    if int < 0 and int > 4:
        print("Please enter a valid input!")
        exit

def going_up():"""




current_floor = int(input("Enter the floor you're on: "))
if current_floor > max_floor or current_floor < min_floor:
    print("Please enter a valid floor!")
#elif current_floor < min_floor:
else:
    number_of_people = int(input("How many are you: "))                                                    #if number_of_people > 1:
    for number in range(number_of_people):                                                                 #print("Enter destination floor: ")        if number < number_of_people:
        destination_floor = int(input("Enter the floor you want to go to: "))
        going_up.append(destination_floor)      #Incase you are going to floor 4, sb else to 3, add that to list and stop when in floor 3
    
    if destination_floor <= 4: 
        for floor in range(destination_floor):
            if current_floor < destination_floor in going_up:
                current_floor += 1
                time.sleep(2)
                print(current_floor)
            if current_floor == destination_floor in going_up:
                print("Floor " +str(destination_floor) + ": Door opens")
                #input("prompt: ") 
                
                #Going down I think.
    if destination_floor < 4 >= 0:
        while current_floor > destination_floor in going_up:
            current_floor -= 1
            time.sleep(2)
            print(current_floor)
        if current_floor == destination_floor in going_up:
            print("You are here in floor " + str(destination_floor) + " now!")
            print("Door opens ")
    input(" ")
                 
    """else:
        print("Enter valid input! ")"""       
    """if destination_floor <= 4: 
        for floor in range(destination_floor):
            if current_floor < destination_floor in going_up:
                current_floor -= 1
                time.sleep(2)
                print(current_floor)
        if current_floor == destination_floor in going_up:
            print("Floor " +str(destination_floor) + ": Door opens")"""

    

    

    
    
