#What we need to do.
"""1.Create a program such that the number of faces in a die are represented by numbers between 0-1
   2.Roll this die 1000 times. The face that comes up should be random
   3.Take the results and tabulate them such that we have the face, number of times in a 1000 it turned up and the frequency.
"""

#1.
import random
from tabulate import tabulate

#Using numbers between 0 and 1 to represent the six phases
total_freq_1 = 0
total_freq_2 = 0
total_freq_3 = 0
total_freq_4 = 0
total_freq_5 = 0
total_freq_6 = 0

for item in range(1000):
    rand_number = random.random()
    if rand_number <=1/6:
        #face = 1
        total_freq_1 += 1
    elif rand_number >1/6 and rand_number <= 2/6:
        #face = 2
        total_freq_2 += 1 
    elif rand_number >2/6 and rand_number <= 1/2:
        #face = 3
        total_freq_3 += 1
    elif rand_number >1/2 and rand_number <= 4/6:
        #face = 4
        total_freq_4 += 1
    elif rand_number >4/6 and rand_number <= 5/6:
        #face = 5
        total_freq_5 += 1
    else: #rand_number >5/6 and rand_number <= 6/6:
        #face = 6
        total_freq_6 += 1

print(total_freq_1)
print(total_freq_2)
print(total_freq_3)
print(total_freq_4)
print(total_freq_5)
print(total_freq_6)

#Percentage_frequency = total_frequency / 1000 * 100
Percentage_frequency_1 = total_freq_1/1000 * 100
Percentage_frequency_2 = total_freq_2/1000 * 100
Percentage_frequency_3 = total_freq_3/1000 * 100
Percentage_frequency_4 = total_freq_4/1000 * 100
Percentage_frequency_5 = total_freq_5/1000 * 100
Percentage_frequency_6 = total_freq_6/1000 * 100

table = [
[1, total_freq_1, Percentage_frequency_1],
[2, total_freq_2, Percentage_frequency_2],
[3, total_freq_3, Percentage_frequency_3],
[4, total_freq_4, Percentage_frequency_4],
[5, total_freq_5, Percentage_frequency_5],
[6, total_freq_6, Percentage_frequency_6]]
headers = ["Faces","Frequency_per_face","Percentage_frequency"]
print(tabulate(table,headers, tablefmt = "fancy_grid"))

    
 