def print_square(side_length):
    """This is function that takes the side_length a paramater"""
    for i in range(side_length): # iterates over the row value of the side length specified by the user
        for j in range(side_length): # iterates over the column of the side length specified by the user
            if i == 0 or i == side_length -1 or j == 0 or j == side_length - 1: # this checks if the position of the iterated rows and colums are at the top, 
                                                                                # bottom, left or right position.
                print("*", end=" ") # This prints the "*" character and an empty space after each character is printed
            else:
                print(" ", end=" ") # this prints an empty space if the first conditional statement is not satisfied it also prints an empty space after each
        print() # this prints am empty line if the conditional statements has been satisfied
        
side_length = int(input("Enter the side length or the square: ")) # This takes the user's input and converts it to an integer and stores it inside the 
                                                                  # *side_length* variable.

print("\nSquare: ")  # this prints a newline character called Square
print_square(side_length) # this calls the function and the argument *side_length* is passed into it.