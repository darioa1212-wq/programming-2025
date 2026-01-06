# Functions
# Author: Ubial
# 8 October

# function to print "hello" to the console
def say_hello():
    print("hello")

# function to print a personalized hello
def say_hello_personal(name="Tiger"):
    print(f"hello {name}!")

def normalized_input():
	"""Clean up the user's input"""
	output = input()
	output = output.strip(",.?! ").lower()
	return output

def some_fun():
    print("hello!")
    return None

def some_fun_return() -> str:
    print("hello!")
    return "purple monkey dishwasher!"
    print("does this run?")

return_val = some_fun_return()
print(return_val)

say_hello_personal("David")
say_hello_personal()
