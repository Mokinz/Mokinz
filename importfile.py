from Imports import *  # * importuje wszystko
import sys
import random
import math
import datetime
import calendar
import os

courses = ["History", "Math", "Physics", "CompSci"]

# Przyklad 1 -implementacja swoich bilbliotek-
index = find_index(courses, "History")
print(index)
print(test)

# print(sys.path)

# Przyklad 2 -standardowa biblioteka losujaca "random"-

random_course = random.choice(courses)
print(random_course)

# Przyklad 3 -standardowa biblioteka operacji matematycznych "math"-
rads = math.radians(90)

print(math.sin(rads))

# Przyklad 4 -standardowa biblioteka "daytime" i "calendar"-
today = datetime.date.today()
print(today)
print(calendar.isleap(2017))

# Przyklad 5 -standardowa biblioteka "os"- dodaje/usuwa pliki, skanuje
print(os.getcwd())  # pokazuje lokalizacje skryptu
