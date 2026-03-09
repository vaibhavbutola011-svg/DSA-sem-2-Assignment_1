'''
Algorithmic Efficieny and Recursive Toolkit (AERT)

This is the python program file for the assignment.
'''

# PART: A -> Stack ADT

# Creating the class StackADT
class StackADT:

    # Calling the constructor
    def __init__(self, stack :list =[]):
        self.stack = stack
    
    # Making the push function
    def push(self, toPush):
        self.stack.append(toPush) # appeding the element to the last of the array (stack)
    
    # Making the pop function
    def pop(self):
        # Condition for checking underflow and popping element only if there exist an element in the stack
        if len(self.stack) > 0:
            self.stack.pop() # removing the last element
        else:
            print("Underflow") 
            return "Underflow"
    
    # Making the peek function
    def peek(self):
        # Checking for the condition that the stack isn't empty
        if len(self.stack) > 0:
            print(self.stack[-1])   # Displaying the last element
            return self.stack[-1]
        else:   
            print("Underflow")
            return "Underflow"

    # Adding function to check whether the stack is empty or not
    def is_empty(self):
        if len(self.stack) == 0:
            print(True)
            return True
        else:
            print(False)
            return False
    
    # Making a function to check the size of the element
    def size(self):
        print(len(self.stack))
        return len(self.stack)
    
# Implementation
# Using Tower of hanoi for implementation
def printMove(source: str, destination: str):
    print(f"Moving the Disk from {source} to {destination}")
    return f"Moving the Disk from {source} to {destination}"

hanoiTower = StackADT()

def hanoi_tower(n: str, source: str, auxiliary: str, destination: str):
    global hanoiTower
    if n == 1:  # Defining the base case
        move = printMove(source, destination)
        hanoiTower.push(move)
        return
    
    hanoi_tower(n-1, source, destination, auxiliary)
    move = printMove(source, destination)
    hanoiTower.push(move)
    hanoi_tower(n-1, auxiliary, source, destination)

# Storing the output in the file
with open('output.txt', "w") as file:
    hanoi_tower(3, 'A', 'B', 'C')
    print(hanoiTower.stack)
    file.write("Output for the StackADT implementation using Hanoi tower problem:\n\n")
    for move in hanoiTower.stack:
        file.write(f"{move}\n")
    file.write("\n----------------------------\n")


# PART: B -> Factorial and Fibonacci

# Factorial Function
def factorial(n: int):
    # Defining the base case as 0 (0! = 1)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Saving the output in the output.txt file
with open("output.txt", "a") as file:
    file.write("\nOutput for Factorial(for n=0, 1, 5 & 10 respectively):\n")
    file.write(f"{factorial(0)}\n")
    file.write(f"{factorial(1)}\n")
    file.write(f"{factorial(5)}\n")
    file.write(f"{factorial(10)}\n")
    file.write("\n----------------------------\n")

# Fibonacci function

# Naive Fibonacci

naive_counter = 0 # counter for recursive calls in naive fibonacci

def fib_naive(n: int):
    global naive_counter
    naive_counter += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_naive(n-1) + fib_naive(n-2)

# Storing the output for fibonacci naive in output.txt file
with open("output.txt", "a") as file:
    file.write("\nOutput for Fibonacci navie mehtod(for n=5, 10, 20 & 30 respectively):\n")
    file.write(f"{fib_naive(5)}\n")
    naive_counter = 0
    file.write(f"{fib_naive(10)}\n")
    naive_counter = 0
    file.write(f"{fib_naive(20)}\n")
    naive_counter = 0
    file.write(f"{fib_naive(30)}\n")
    file.write("\n----------------------------\n")

# Memoized Fibonacci
memo = {}   # Memoization dictionary

memo_counter = 0 # counter for the recursive calls in memoized fibonacci

# Fibonacci function using memoization
def fib_memo(n: int):
    global memo, memo_counter
    memo_counter += 1
    if n == 0:
        if n not in memo.keys():
            memo[n] = 0
        return memo[n]
    elif n == 1:
        if n not in memo.keys():
            memo[n] = 1 
        return memo[n]
    else:
        if n not in memo.keys():
            memo[n] = fib_memo(n-1) + fib_memo(n-2)
        return memo[n]

# Storing the output in the output.txt file
with open("output.txt", "a") as file:
    file.write("\nOutput for Fibonacci memoized mehtod(for n=5, 10, 20 & 30 respectively){considering memo_counter to update after each call to 1 and memo dictionary to empty after each function run as they both are global}:\n")
    file.write(f"{fib_memo(5)}\n")
    memo, memo_counter = {}, 0 
    file.write(f"{fib_memo(10)}\n")
    memo, memo_counter = {}, 0 
    file.write(f"{fib_memo(20)}\n")
    memo, memo_counter = {}, 0 
    file.write(f"{fib_memo(30)}\n")
    memo, memo_counter = {}, 0 
    file.write("\n----------------------------\n")

# PART: C -> Tower of Hanoi problem

# Making the hanoi auxiliary function to print the moves
def printMove(n:int ,source: str, destination: str):
    print(f"Move disk {n} from {source} to {destination}")

tower_of_hanoi_output_str = "" # Made extra variable for the sake of storing data in the output file

# Making the hanoi function
def hanoi(n: int, source: str, auxiliary: str, destination: str):
    global tower_of_hanoi_output_str
    if n == 1:  # Defining the base case
        printMove(n, source, destination)
        tower_of_hanoi_output_str += f"\nMove Disk {n} from {source} to {destination}"
        return 
    
    hanoi(n-1, source, destination, auxiliary)
    printMove(n, source, destination)
    tower_of_hanoi_output_str += f"\nMove Disk {n} from {source} to {destination}"
    hanoi(n-1, auxiliary, source, destination)

hanoi(3, 'A', 'B', 'C')

# Storing the output in the output.txt file
with open("output.txt", "a") as file:
    file.write("\nOutput for the Tower of hanoi problem:\n")
    file.write(tower_of_hanoi_output_str+"\n")
    file.write("\n----------------------------\n")


# PART: D -> Recursive Binary search
# Defining the function
def binary_search(arr: list, key: float, low: int, high: int):

    # Defining the base case
    if low > high:
        return -1

    mid = (low + high) // 2 # Finding out the middle

    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)

arr = [1,3,5,7,9,11,13]
print(binary_search(arr, 7, 0, (len(arr) - 1) ))
print(binary_search(arr, 1, 0, (len(arr) - 1) ))
print(binary_search(arr, 13, 0, (len(arr) - 1) ))
print(binary_search(arr, 2, 0, (len(arr) - 1) ))
arr = []
print(binary_search(arr, 7, 0, len(arr) - 1))

# Storing the data in the output.txt file
with open("output.txt", "a") as file:
    arr = [1,3,5,7,9,11,13]
    file.write("\nThis is the output of binary search using recursion method:\n")
    file.write("For arr = [1,3,5,7,9,11,13] and key=7, 1, 13 & 2 respectively\n")
    file.write(f"{binary_search(arr, 7, 0, (len(arr) - 1) )}\n")
    file.write(f"{binary_search(arr, 1, 0, (len(arr) - 1) )}\n")
    file.write(f"{binary_search(arr, 13, 0, (len(arr) - 1) )}\n")
    file.write(f"{binary_search(arr, 2, 0, (len(arr) - 1) )}\n")
    file.write("\nFor arr = [] and key = 7\n")
    arr = []
    file.write(f"{binary_search(arr, 7, 0, (len(arr)-1))}\n")
    file.write("\n----------------------------\n")

