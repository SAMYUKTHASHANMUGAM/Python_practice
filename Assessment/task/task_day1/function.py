#Functional programming

#creating function for upper
def shout(text): 
    return text.upper() 

#creating function for lower  
def whisper(text): 
    return text.lower() 

#creting function for getting user input
def greet(func): 
    # storing the function in a variable 
    greeting = func("Good morning everyone present here!!") 
    print(greeting)  
  
greet(shout) #print at first
greet(whisper) #print at second