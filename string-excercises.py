#Excercise 2.3

your_name = "Jim"
message = f"Hello {your_name}, do you like to learn some Python?"
print(message)

#Excercise 2.4

message_lower_case = f"Hello {your_name.lower()}, do you like to learn Python?"
print(message_lower_case)

message_upper_case = f"Hello, {your_name.upper()}, do you like to learn Python?"
print(message_upper_case)

meesage_title_case = f"Hello, {your_name.title()}, do you like to learn Python?"
print(meesage_title_case)

# Excercise 2.5

famous_quote = 'Aristotle once said "Quality is not an act, it is a habit."'
print(famous_quote)

# Excercie 2.6

famous_person = "Aristotle"
message = f'{famous_person} once said, "Quality is not an act, it is a habit." '
print(message)

# Excercie 2.7

person_with_tabs = "\tAristotle\t"
person_with_new_line = "\nAristotle"

print(person_with_tabs.lstrip())
print(person_with_tabs.rstrip())
print(person_with_tabs.strip())


print(person_with_new_line)
print(person_with_new_line.rstrip())
print(person_with_new_line.strip())

#Excercids 2.8

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))