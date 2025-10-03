name = input("Hello, what's your name? ")
print(name + " it is a pleasure to meet you.")
age = input("And how old are you " + name + "? ")
cleaned_age = int(age)
year_born = 2025 - cleaned_age
print("So, you were born in", year_born)
