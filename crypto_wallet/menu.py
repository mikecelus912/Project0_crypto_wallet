# create a command-line menu where the user can input
# choose to either create a new user profile or login with their
# current credentials
def menu():
    print("\n--------MAIN MENU-----------")
    print("[1] Create New User")
    print("[2] Login to User")
    print("[0] Exit")
    print("-----------------------------")


# create a submenu for a logged-in user to update and/or delete their profile
def sub_menu():
    print("\n------You are Logged In--------")
    print("[3] View Wallet")
    print("[4] Find Crypto prices")
    print("[5] Update User")
    print("[6] Delete User")
    print("[0] Return to Main")
    print("-----------------------------")