student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_df = pd.read_csv(r"day26\NATO-alphabet-start\NATO-alphabet-start\nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def control_user_input():
    user_name = input("Translate to NATO: ") or "n"
    try:
        user_NATO_name = [nato_dict[l] for l in user_name.upper()]
    except KeyError:
        print("Sorry, only letters are accepted.")
        control_user_input()
    else:
        print(user_NATO_name)

control_user_input()