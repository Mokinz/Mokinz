# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

# False Values:
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.

# Program 1
# language = "Java"

# if language == "Python":
#     print("Language is Python")
# elif language == "Java":
#     print("Language is Java")
# elif language == "JavaScript":
#     print("Language is JavaScript")
# else:
#     print("No Match")

# Program 2
# user = "Admin"
# loggeed_in = False

# if not loggeed_in:
#     print("Please log in")
# else:
#     print("Welcome")

# Program 3
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
print(a is b)  # is sprawdza id  print(id(s) == id(b)) - True
