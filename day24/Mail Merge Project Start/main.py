#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r"day24\Mail Merge Project Start\Input\Names\invited_names.txt") as names:
    for name in names.readlines():
        with open(r"day24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as start_letter:
            temp_letter = ""
            for line in start_letter.readlines():
                temp_letter += line   
        temp_letter = temp_letter.replace("[name]", name.strip())
        with open(f"day24/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name.strip()}.txt", "w") as output:
            output.write(temp_letter)
