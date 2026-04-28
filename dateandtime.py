#Question 3: 150 QUESTIONS IN PYTHON SERIES

#HOW TO DISPLAY CURRENT DATE AND TIME
#import the 'datetime' module to work with date and time
import datetime 

#Get the current date and time
now = datetime.datetime.now()

#Create a datetime object representing the current date and time 
#Display a message indicating what is being printed 

print("Current date and time:")
#Print the current date and time in a specific format 
print(now.strftime("%Y-%m-%d %H:%M:%S"))
