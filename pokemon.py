#PYTHON PROJECT 10: Pokemon Training Game 

#A pokemon trainer catches Pokemon one by one, each having a power level represented by
# a positive integer.
#After every catch, the trainer updates the collection and displays the 
#minimum and maximum power levels among all Pokemon caught so far 
#to track the team's strength. 

#for example
#input: pokemon powers caught in order - 3 8 9 7
#Output: 3 3, 3 8, 3 9, 3 9
#Explanation
#After catching Pokemon with power 3 -> min = 3, max = 3
#After catching Pokemon with power 8 -> min = 3, max = 8
#After catching Pokemon with power 9 -> min = 3, max = 9
#After catching Pokemon with power 7 -> min = 3, max = 9

powers = [3, 8, 9, 7] #creates a list of Pokemon power levels
mini = maxi = powers[0]
print(mini, maxi)

for power in powers[1:]: #loops through the remaining Pokemon starting from the second one
    mini = min(mini, power) #updates mini if the current Pokemon's power is smaller than the previous minimum
    maxi = max(maxi, power) #updates maxi if the current Pokemon's power is greater than the previous maximum
    print(mini, maxi)