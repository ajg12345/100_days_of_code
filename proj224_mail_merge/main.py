#TODO: Create a letter using starting_letter.txt 
with open('./Input/Letters/starting_letter.txt', 'r') as sl:
    sl_text = sl.read()

with open('./Input/Names/invited_names.txt', 'r') as iv_n:
    names = iv_n.readlines()

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
for name in names:
    proper_name = name.strip()
    with open(f'./Output/ReadyToSend/{proper_name}.txt', 'w') as current_letter:
        current_letter.write(sl_text.replace('[name]', proper_name))

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp