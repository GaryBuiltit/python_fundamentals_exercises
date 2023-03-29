string = "string"

"""
with negative indices it allows for you 
to work with data structures like strings 
and list from reverse with -1 being the last 
character, -2 the second to last character and so on.

example 1: with a -2 on the left side 
of the colon it slices starting at the seconf to last character

example 2: with the -2 on the right side of the 
colon it will end the slice at the second to last character.
it will not include that character so it will actually 
include all characters before the second to last character.
"""

print(string[-2:])  # example 1
print(string[:-2])  # example 2
