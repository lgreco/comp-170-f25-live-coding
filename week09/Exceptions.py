def is_int(string: str) -> bool:
    # Initialize return variable to answer this question:
    # is the input string something I can work with, ie,
    # non None and not empty?
    answer = string is not None and len(string) > 0
    i = 0
    while answer and i < len(string):
        # Now ask this question: is the current character
        # of the input string a numeric symbol? (0-9)
        answer = '0' <= string[i] <= '9'
        i += 1
    # When does this loop stop?
    return answer


good_data = False
tries = 0
OLDEST = 130

while not good_data and tries < 3:
    year_born = input("\nWhat year were you born? ")
    good_data = is_int(year_born) and 2025-int(year_born) < OLDEST
    if good_data:
        age = 2025-int(year_born)
        print(f"\nSo, you are {age} years old!\n")
    else:
        print("\nYou are supposed to type an int number within the last 150 years. Try again.")
    tries += 1