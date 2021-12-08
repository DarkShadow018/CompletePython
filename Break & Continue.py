student = ["ram", "shyam", "radha", "radhika", "mohan", "ganesh", "aditya", "ramesh"]
for student in student:

    if student == "mohan":
        continue;#This will skip mohan and continue to print the next name

    if student == "aditya":
        break;#This will break the loop and terminate consicutive commands
    print(student)