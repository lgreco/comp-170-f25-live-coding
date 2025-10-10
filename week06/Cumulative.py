# DO NOT CODE LIKE THIS .. I will find you wherever you are
# and take back any diploma LUC awards you. 

def coffee_choice():
    today = input("\nWhat day is today? ")

    if today == "Monday":
        print("Have a single espresso")
    elif today == "Tuesday":
        print("Have a plain latte")
    elif today == "Wednesday":
        print("Have a pumpkin spice latte, you hipster you!")
    elif today == "Thursday":
        print("Have a cortado")
    elif today == "Friday":
        print("Have some tea for a change")
    elif today == "Saturday":
        print("Have a doppio")
    else:
        print("On a Sunday, have a lavender latte")

def determine_parity():
    n = int(input("Give me an integer, any integer... "))
    if n % 2 == 1:
        print(f"{n} is an odd number")
    else:
        print(f"{n} is an even number")


print((10*20+58)/11)