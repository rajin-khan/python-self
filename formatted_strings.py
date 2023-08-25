first = "Rajin"
last = "Khan"
message = first + " [" + last + "] is a coder"
print(message)
#while this is fine, it's pretty nooby, and you can achieve the same result with a formatted string. the format is:
msg = f"{first} [{last}] is a coder" #the curly braces act like placeholders for the variables. a formatter string in code begins
#with f and has the string in double quotes.
print(msg)