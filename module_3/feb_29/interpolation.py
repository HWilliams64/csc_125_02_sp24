grocery_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]
capitalized_grocery_list = []

# Keep reading items until there are no more items left
for item in grocery_list: 
    # read an item and remember it in its capitalized form
    capitalized_item = item.title()

    # write it down on the other paper
    capitalized_grocery_list.append(capitalized_item)

print(capitalized_grocery_list)

# Interpolation

# This does the same thing as the previous for loop above, but with a single line
capitalized_grocery_list_2 = [item.title() for item in grocery_list]
print(capitalized_grocery_list_2)

# This does the same thing as the above list but only selects if the
# if-statement is true
capitalized_grocery_list_3 = [item.title() for item in grocery_list if 'a' in item]
print(capitalized_grocery_list_3)

# Aggregation
# map() - this function takes a iterable of items and converts item into another form
# filter() - this function takes a iterable of items and removes items that
# don't match a filter
# sorted() - this function takes an iterable of items and sorts them

# Same as the anonymous function `lambda item: 'a' in item`
def func(item):
    return 'a' in item

print("="*20)
print(grocery_list)
# aggregated_form = filter(lambda item: 'a' in item, map(lambda item: item.title(), grocery_list))
aggregated_form = map(lambda item: item.title(), filter(lambda item: 'a' in item, grocery_list))

for item in aggregated_form:
    print(item)