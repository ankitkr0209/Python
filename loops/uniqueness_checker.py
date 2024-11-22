


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()
duplicates = set()

for item in items:
    if item in unique_item:
        duplicates.add(item)  # Add to duplicates if already seen
    else:
        unique_item.add(item)  # Add to unique_item if not seen

# Print the duplicates
if duplicates:
    print("Duplicate items:", duplicates)
else:
    print("No duplicates found.")

print(unique_item)
