#Python Project 15: Password Strength Checker

import re 

def check_password_strength(password):
    ''' checks the strength of a password based on common criteria
    returns feedback on missing requirements '''
    
    #Criteria flags 
    
    length_ok = len(password) >= 8
    has_uppercase = re.search(r'[A-Z]', password) is not None 
    has_lowercase = re.search(r'\d', password) is not None 
    #Special characters check using a common set 
    has_special = re.search(r'[!"£$%^&*()@]', password) is not None 
    has_digit = re.search(r'\d', password) is not None
    
    feedback = []
    
    if not length_ok:
        feedback.append("Password must be at least 8 characters long.")
    if not has_uppercase:
        feedback.append("Password must contain at least one uppercase letter.")
    if not has_lowercase:
        feedback.append("Password must contain at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password must contain at least one digit")
    if not has_special:
        feedback.append("Password must contain at least one special character")
        
    if not feedback:
        return "Password is strong!"
    else:
        return "Password is weak. Please improve it with the following:\n" + "\n".join(feedback)
        
#Example usage:
password = input("Enter a password")
strength_feedback = check_password_strength(password)
print(strength_feedback)