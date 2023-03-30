# Read in payloads from a file
with open("payloads.txt", "r") as f:
    payloads = f.read().splitlines()

# Get user input for replacement string
replace_str = input("Enter the replacement string: ")

# Replace "[redirect]" with user input in each payload
new_payloads = []
for payload in payloads:
    new_payload = payload.replace("[redirect]", replace_str)
    new_payloads.append(new_payload)

# Write new payloads to a file
with open("new_payloads.txt", "w") as f:
    f.write("\n".join(new_payloads))
