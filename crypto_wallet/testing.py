# def get_ssn():
#
#     ssn = input("enter SSN (ddd-dd-dddd):")
#     ssn_sections = ssn.split('-')
#     valid = False
#
#     if len(ssn_sections) == 3:
#         if len(ssn_sections[0]) == 3 and len(ssn_sections[1]) == 2 and len(ssn_sections[2]) == 4:
#             valid = True
#         print("Valid")
#     else:
#         print("Not a valid SSN")
#
# get_ssn()

# use random names and values to populate the User collection
# for i in range(2):
#     random_first_name = names.get_first_name()
#     random_last_name = names.get_last_name()
#     random_ssn = int(1000000000 * random.random())
#     random_username = names.get_full_name()
#     random_password = os.urandom(16)
#     db.Users.insert_one({"First Name": random_first_name,
#                          "Last Name": random_last_name,
#                          "SSN": random_ssn,
#                          "Username": random_username,
#                          "Password": random_password
#                          })





