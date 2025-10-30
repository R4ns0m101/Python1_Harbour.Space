# Create a list from 1-100
# Remove the odd number that is divisple by 3
# Print final_list
# Count how many numbers left

my_list = []

for index in range(1,101):
    my_list.append(index)

for index in range(1,101):
    if index % 2 == 1:
        if index % 3 ==0:
            my_list.remove(index)
        else:
            continue
    else:
        continue
print("Final list is", my_list)
print("Final list has", len(my_list), "elements")