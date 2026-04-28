#Python Project 23: Converting an emoji into text 

#Example 1: Remove emojis from text
import demoji 
text = "Good Morning!🥰"
a1 = demoji.replace(text, "")
print(a1)

#Example 2: Replace emojis with descriptive text
text = "Happy Birthday! 🥰"
a1 = demoji.replace_with_desc(text)
print(a1)

#Example 3: Detect Emojis in a String 
text = "Good Morning! 🥰"
emojis = demoji.findall(text)
print(emojis)

#Example 4: Remove all emojis from text 
text = "Welcome to the party!🥰"
a1 = demoji.replace(text, "")
print(a1)


