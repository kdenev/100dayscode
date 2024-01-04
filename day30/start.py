# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open(r"day30\a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(error_message)
# else:
#     content= file.read()
#     print(content)
# finally:
#     raise TypeError("I made this up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)