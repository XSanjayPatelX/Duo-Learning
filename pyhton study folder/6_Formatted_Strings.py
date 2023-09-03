# useful in situations when you want to dynamically generate some text with your variables
first = "John"
last = "Smith"
message = first + " [" + last + "] is a coder" # it is not ideal because the text gets harder to read
msg = f"{first} [{last}] is a coder" # this is a formatted string. Curley braces defining placeholders or holes in string.
# They will be filled in with values of our variables
# prefix your string with an "f" and use curley braces to dynamically place insert values into string - line 5
print(message)
print(msg)