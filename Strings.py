name = "Tony Stark"

print("Hello, your name is", name)
print("Hello, your name is", name.upper() + " in uppercase")
print("Hello, your name is", name.lower() + " in lowercase")
print("The letter is found at index", name.find('y'))
print("The letter is found at index", name.find('Tony'))
#Only first letter is searched so the index is 0
print("The letter is found at index", name.find('Y'))
#If the letter is not found in the string then the index will be -1
print("Hello, my name is", name + " and I'm", name.replace("Tony Stark", "Iron Man"))