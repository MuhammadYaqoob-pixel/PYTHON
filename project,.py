
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print(f"\nMultiplication Table ({rows} x {cols})\n")

# Print the table header
print("    ", end="")
for i in range(1, cols + 1):
    print(f"{i:4}", end="")
print("\n" + "-" * (cols * 4 + 4))

# Generate the table using nested loops
for i in range(1, rows + 1):
    print(f"{i:2} |", end="")  # Row label
    for j in range(1, cols + 1):
        print(f"{i * j:4}", end="")  # Multiplication result
    print()
