import re

# Load valid-tld list
with open("domain_list.txt", "r") as file:
    tld_list = file.readlines()

expression = "\w+@{1}[a-zA-Z]+\.{1}[a-zA-Z]{1-4}"
email = input("Type your email -> ")

validator = re.fullmatch(expression, email)
if validator is not None:
    print(f"Your email parsed is -> {validator.string}")
else:
    print("Not a valid email!")