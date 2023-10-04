
#!
#?
# TODO:
# *

#* Literal assignment
first = "Dave"
last = "Gray"
print (type(first))
print (type(first)==str)

#? Constructor Function Example
pizza = str("Cheese")
print(type(pizza))
print(type(pizza) == str)

#? Concatenation
fullname = first + " " + last
print(fullname)

#? Casting a number to a string
decade = str(1980)
print(type (decade))
statement = "I like the rock music from the "+ decade+"s."
print(statement)

#? Multiple lines
multiline = """
How are you?

I was just cheking in
"""
print(multiline)

#? Escaping special characters
sentence = 'I\'m Vivek \t Hey! \n\nWhere\'s this at \\located?'
print (sentence)
