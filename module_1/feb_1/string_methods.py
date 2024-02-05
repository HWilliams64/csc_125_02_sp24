# We want to remove "jumped"
my_sentence = "The dog jumped over the car"
# [start:stop:step]
start = my_sentence[:8]
end = my_sentence[14:]
print(f"'{start}' '{end}'")
print(start+end)

# Using the replace method
jump_removed = my_sentence.replace("jumped", "")
print(jump_removed)

title = my_sentence.title()
print(title)

upper = my_sentence.upper()
print(upper)

lower = my_sentence.lower()
print(lower)

lower = my_sentence.casefold()
print(lower)

# harris@bhcc.edu
# Harris@bhcc.edu
# hArris@bhcc.edu
