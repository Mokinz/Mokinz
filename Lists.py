

# Mutable - czyli mozna manipulowac lista
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)


# # Immutable - czyli nie da sie zmienic danych, mozna je tylko odczytac
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets - nie dbaja o kolejnosc elementow - sluza glownie do wylaczenia powtorzen oraz 
# sprawdzeniu czy dany element jest w zbiorze
# cs_courses = {'History', 'Math', 'Physics', 'CompSci'}

# print(cs_courses)

# ########################################################################

# # Empty Lists
# empty_list = []
# empty_list = list()

# # Empty Tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty Sets
# empty_set = {} # This isn't right! It's a dict
# empty_set = set()