n = int(input("\n\nHow many values to process? "))
sum = 0 # initialize accumulator
for i in range(n):
    x = int(input("\n enter a value: "))
    sum = sum +x
average = sum/n
print(f"\nThe average is {average:.2f}")