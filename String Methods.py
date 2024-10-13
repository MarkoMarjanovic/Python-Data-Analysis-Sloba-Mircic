# capitalize - adds a capital letter (only 1st letter affected)
variable = 'hello'
print(variable.capitalize()) # Hello

# casefold - converts all to lower case, usefull when comparing strings if needed
variable = 'HeLLO'
variable2 = 'HELlo'
print(variable.casefold()) # hello
print(variable.casefold()) # hello

# center - centers the text, additionally you can add a string as the argument
# to specify which strings are going to occupy added spaces on the sides
variable = 'Hello'
print(variable.center(20)) # occupies 20 spaces total
print(variable.center(20, '.')) # 20 spaces total and the text is centered around dots (......Hello......)

# count
variable = 'abc_abc_abc'
print(variable.count('ab')) # 3, returns the number of times the specified string appears in the variable

# encode
variable = 'Elon Musk'
print(variable.encode(encoding = 'utf-8', errors = 'strict')) # encodes and returns an error in case the encoding doesnt work

# endswith
variable = 'Apple'
print(variable.endswith('e')) # Returns True or False based on the last letter of the string

# expandtabs
variable = 'text\ttext2\ttext3' # \t creates a Tab
print(variable.expandtabs(20)) # expands the Tab value to 20 in this case

# find
variable = 'Please like and subscribe'
position = variable.find('subscribe') # define a variable that will hold an index position of the string where the string we are looking for is
print(position) # It will show number 16
print(variable[position:]) # in order to get the actual work, we need to find it by the index and print from there

# format
# Method 1
text = '{subject} is doing: {action}'
print(text.format(subject = 'Cat', action = 'Meow'))
# Method 2
text2 = '{} is doing: {}'
print(text2.format('Cat', 'Meow'))

# index
content = 'Are there bananas on the moon'
position = content.index('bananas') # creates an index number of the word bananas, similar to find
print(position) # shows the index number of the word
print(content[position:]) # prints the word and all the text after the word, same like find

# isalnum
text = 'hellokitty123'
print(text.isalnum()) # checkes if the text is alphanumeric, if any exclamation or special characters exist, returns False

# isalpha
text = 'hellokitty'
print(text.isalpha()) # checks if the text is alpha only, returns False if it is not

# isascii
text = 'hellokitty'
print(text.isascii()) # checks if the text is ascii, returns false if it is not

# isdecimal
text = '123'
print(text.isdecimal()) # checks if the string contains numbers (similar isdigit and isnumeric methods)

# isidentifier
text = '1text-sample'
print(text.isidentifier()) # checks if the string is possible to use as a variable name True and False results

