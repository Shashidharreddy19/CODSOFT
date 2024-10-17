names_list = []
phone_numbers_list = []
number_of_entries = 3
for _ in range(number_of_entries):
    name = input("enter the valid name: ")
    phone_number = input("enter the valid phone no: ")  # Convert to int if needed using int(input("Phone Number: "))
    names_list.append(name)
    phone_numbers_list.append(phone_number)
print("\nname\t\t\tphone number\n")
for i in range(number_of_entries):
    print(f"{names_list[i]}\t\t\t{phone_numbers_list[i]}")
search_term = input("\nEnter search term: ")
print("Search for the  result:")
if search_term in names_list:
    index = names_list.index(search_term)
    phone_number = phone_numbers_list[index]
    print(f"Name: {search_term}, Phone Number: {phone_number}")
else:
    print("Name that you entered is not found")