SIZE = 1

for line in range(1, SIZE +2):
    print(" " * (SIZE), end="")
    print("||")
for line_2 in range(SIZE - 1):
    print("*" * (line - SIZE + 1), end="")
    print("||", end="")
    print("*" * (line - SIZE + 1))
print(" " * (SIZE - 1), end="")
print("=" * SIZE * 2)

