# SHORTCUTS
# ctrl + / = comment & uncomment line
# shift + enter = koniec linijki i zejscie do kolejne
# ctrl + right/left arrow key = przeskoczenie o slowo
# highlated line + ctrl + up/down arrow key = przsuniecie bloku gora/dol
# highlated line + Tab (+Shift) = akapit (wciecie tekstu)

# DICTONARIES

student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}

# age = student.pop("age")

student.update({"name": "Jane", "age": 26, "phone": "555-555"})

# print(student)
# print(age)
print(student.items())

for key, value in student.items():
    print(key, value)
