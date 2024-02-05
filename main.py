import re

expression = "\w+@{1}[a-zA-Z]+\.{1}[a-zA-Z]+"
email = input("Type your email -> ")

validator = re.fullmatch(expression, email)
if validator is not None:
    print(f"Your email parsed is -> {validator.string}")
else:
    print("Not a valid email!")