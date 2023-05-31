#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        
abs_path = 'day24_mail_merge/project/'

with open(abs_path+'Input/Letters/starting_letter.txt', mode='r') as file:
    starting_letter = file.read()
    
with open(abs_path+'Input/Names/invited_names.txt', mode='r') as file:
    names = file.read()
names = names.splitlines()
# This could have been one line less if I read the hints

for name in names:
    single_letter = starting_letter.replace('[name]', name)
    with open(abs_path+f'Output/ReadyToSend/letter_for_{name.lower()}.txt', mode='w') as file:
        file.write(single_letter)