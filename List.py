marks = [98, 86, 99, 85, 96, 83, 91, 87, 88]
print(marks)
print(marks[2])
print(marks[4])#Printing 5th character
print(marks[-2])
print(marks[-4])#Printing 6th character
print(marks[-5])#Printing 5th character
print(marks[0:2])#Index 2 which means 3 character of the list will not be included

marks.append(90)
marks.insert(1, 91)
print(91 in marks)
print(61 in marks)

for score in marks:
    print(score)
print(len(marks))

#Printing marks using while loop

i = 0
while i < len(marks):
    print(marks)
    i += 1

i = 0
while i < len(marks):
    print(marks[i])
    i += 1

marks.clear()
print(marks)

#Note : [] Makes a List, () Makes a Tuple, {} Makes a Set