to_do_list = ["math homework", "research for biology", "clean the room", "fun"]
first_item = to_do_list[0]  # Accesses the first item at index 0, which is "math homework"
second_item = to_do_list[1]  # Accesses the second item at index 1, which is "research for biology"
third_item = to_do_list[2]  # Accesses the third item at index 2, which is "clean the room"
fourth_item = to_do_list[3]  # Accesses the fourth item at index 3, which is "fun"

print(first_item)
print(second_item)
print(third_item)
print(fourth_item)

shopping_list = ["apples", "bananas", 3, 4.5]  # different data types

# Adding "oranges" to the end of the list (with .append)
shopping_list.append("oranges")
print(shopping_list)

# Adding "lemons" to the third position of the list (with .insert)
shopping_list.insert(2, "lemons")

# Now the list contains ["apples", "bananas", "lemons", 3, 4.5, "oranges"]
print(shopping_list)

# Removing data from "to_do_list"

# Removing "research for biology" by specifying its value (with .remove)
to_do_list.remove("research for biology")
print(to_do_list)

# now the list is ['math homework', 'clean the room', 'fun']

# Removing the item at index 2, which is "fun"
del to_do_list[2]
print(to_do_list)

# Update Values

# Changing the first element (index 0 ) from "math homework" to "physics homework"
to_do_list[0] = "physics homework"

print(to_do_list)  # Output: ['physics homework', 'clean the room']

# 2
favorite_colors = ["red", "green", "blue", "yellow", "purple"]

fourth_color = favorite_colors[3]  # Accces the fourth color at index 3
print(fourth_color)