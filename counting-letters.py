# This code ask to write a phrase or word and show
# the 3 most appearing letters

current_letter = ""    # Letter used in the loop 
times_current_letter = 0   # Amount of times the current letter appeared
times_previous_letter = 0    # Check if the previous letter had more appearences than the current one
most_shown_letter = ""    # First letter that appeared the most
secound_most_shown_letter = ""    # If there is a second that appeared the same number of times
third_most_shown_letter = ""   # If there is a third that appeared the same number of times
amount_most_shown_letter = 0 # Amount of times the letter appeared
counter = 0    # Counter for the iteration
phrase = "" # User input

phrase = input("Write a phrase or word: ").lower()

# Cicle that verify, letter to letter, how many times it appears
while counter < len(phrase):
    current_letter = phrase[counter]
    times_current_letter = phrase.count(current_letter)
    
    # Discarting empty spaces from consideration
    if current_letter == " ":
        counter += 1
        continue
    
    # Here the application will identify if the current letter with the most uses
    # is different from another letter that also have the same number of uses
    # That way, up to 3 different letters with the same number can be identified
    if times_current_letter == times_previous_letter and current_letter != most_shown_letter:
        if secound_most_shown_letter == "":
            secound_most_shown_letter = current_letter
        
        elif current_letter != secound_most_shown_letter and third_most_shown_letter == "":
            third_most_shown_letter = current_letter
        
        else:
            counter += 1
            continue
    
    # Place to store the amount of times the most used letter have
    if times_current_letter > times_previous_letter:
        most_shown_letter = current_letter
        amount_most_shown_letter = times_current_letter
        times_previous_letter = times_current_letter
    
    counter += 1

# Show of the results depending on the number of letters the software identified
if third_most_shown_letter != "":
    print(f'The three most appearing letters were "{most_shown_letter}", "{secound_most_shown_letter}",' \
        f' and "{third_most_shown_letter}", which appeared {amount_most_shown_letter} times each. ')
    
elif secound_most_shown_letter != "":
    print(f'The two most appearing letters were "{most_shown_letter}" and "{secound_most_shown_letter}",' \
        f' which appeared {amount_most_shown_letter} times each. ')
    
else:
    print(f'The letter that appeared the most was "{most_shown_letter}",'  
        f' which appeared {amount_most_shown_letter} times. ')