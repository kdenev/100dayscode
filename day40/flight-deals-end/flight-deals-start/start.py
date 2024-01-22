
print("Welcome to Flifht Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n") or None
last_name = input("What is your last name?\n") or None
email_1 = input("What is your email?")
email_2 = input("Type your eamil again.")

if email_1 == email_2:
    print("You're in the club!")
else:
    print('Start again, emails do not match.')