# Parse through the portions of an email address and print out the username and domain name.
# Name: Coleman Lau
# Date: Sept. 18, 2026

# Method 1: Using split()
email_address = input("Enter an email address: ")
parts = email_address.split("@")
username = parts[0]
domain_name = parts[1]

print("The parts are:", parts)
print("Username:", username)
print("Domain name:", domain_name)

# Method 2: Using index() and slicing
at_sign_index = email_address.index("@")
username2 = email_address[:at_sign_index]
domain_name2 = email_address[at_sign_index + 1:]

print("Username (Method 2):", username2)
print("Domain name (Method 2):", domain_name2)