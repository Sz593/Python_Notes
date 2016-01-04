#! python3

# This program writes out the Collatz sequence for any number.
# This is a mathematical sequence that takes an integer and always
# ends up at 1. 


# Define the next number in the Collatz sequence
def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n)+1

# Ask for a number and start the sequence
print('Enter a number:')
while True:
    try:
        x = int(input())
        break
    except ValueError:
        print('Please enter an integer value.')

while x != 1:
    x = collatz(x)
    print(x)
