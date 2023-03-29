
# Update the arguments for the range function such that when the iteration variable amount_loaded is printed inside the for loop, it will print the values from 0 to 100 (inclusive), incrementing by 5.
# Run your code. At this point, the output should be:

#     Now, inside the for loop, add conditional statements to check when amount_loaded is equal to 25, 50, 75 and 100, such that:
#         If amount_loaded is equal to 25, print "1/4 of the way there"
#         Else, if amount_loaded is equal to 50, print "1/2 of the way there"
#         Else, if amount_loaded is equal to 75, print "3/4 of the way there"
#         Else, if amount_loaded is equal to 100, print "Loading complete!"

# Once you save it and run it, it should look like this:


for amount_loaded in range(0, 101, 5):
    print(amount_loaded)
    if amount_loaded == 25:
        print("1/4 of the way there")
    elif amount_loaded == 50:
        print("1/2 of the way there")
    elif amount_loaded == 75:
        print("3/4 of the way there")
    elif amount_loaded == 100:
        print("Loading is complete!")
