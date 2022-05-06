# import packages needed for this project
import pymongo
import requests
import pandas
import random
import names
from menu import *


# define a main function that can then be run as a script in the main.py file
def main():

    # create variables for the application database along with connection information
    db_name = "Project0"
    db_host = "mongodb://localhost:27017/"

    # a try and exception to determine whether a connection has been established
    try:
        client = pymongo.MongoClient(db_host)
        db = client[db_name]
        print("Database connected!")

    except Exception as e:
        print("Database connection error!")
        raise e

    # with a connection established it is time to connect to CoinGecko API
    # this is an open API for cryptocurrency information
    crypto_prices = requests.get("https://api.coingecko.com/api/v3//coins/markets?vs_currency=usd&order="
                                 "market_cap_desc&per_page=100&page=1&sparkline=false")

    # store the information in a json file
    crypto_prices = crypto_prices.json()

    # now create the collection that will be utilized to store the API request
    db_crypto_prices = db.get_collection("crypto_prices")
    inserted = db_crypto_prices.insert_many(crypto_prices)
    print(str(len(inserted.inserted_ids)) + " documents inserted")

    # use random names and values to populate the User collection
    # for i in range(5):
    #     random_first_name = names.get_first_name()
    #     random_last_name = names.get_last_name()
    #     random_ssn = int(1000000000 * random.random())
    #     random_username = names.get_full_name()
    #     random_password = int(100 * random.random())
    #     db.Users.insert_one({"First Name": random_first_name,
    #                          "Last Name": random_last_name,
    #                          "SSN": random_ssn,
    #                          "Username": random_username,
    #                          "Password": random_password
    #                          })

    # call the menu function
    menu()
    option = str(input("Please enter your option using the correct numeric key: "))

    # utilize a conditional loop which will continue to execute based on user inputs
    while option != "0":
        if option == "1":
            print("You have selected to create a new user profile")

            # insert function to gather user inputs that will become documents in the User collection
            def insert():
                try:
                    first_name = input("Enter your first name: ")
                    last_name = input("Enter your last name:")
                    dob = input("Enter your date of birth in 'YYYY-MM-DD' format: ")
                    ssn = input("Enter your 9-digit Social Security Number: ")
                    username = input("Create a new username: ")
                    password = input("Create a password: ")

                    db.Users.insert_one(
                        {
                            "First Name": first_name,
                            "Last Name": last_name,
                            "Date of Birth": dob,
                            "SSN": ssn,
                            "Username": username,
                            "Password": password
                        }
                    )
                    print("\nUser Data entered successfully!")

                except Exception as e:
                    print("User Profile creation error!")
                    raise e

            # call the insert function
            insert()

        # option 2 will allow previously registered users to log in with their username and password credentials
        elif option == "2":
            print("\nYou have selected to login to your user profile")

            # define a check function to compare username/password input against information stored in the database
            # correctly entered username and password information allows the user to log in to their account
            def check():
                try:
                    login = False

                    # create empty lists for usernames and passwords
                    usernames = []
                    passwords = []

                    # iterate through the Users collection, specifically Username and Password
                    # store the values in the previously created empty lists
                    for results in db.Users.find():
                        usernames += [results["Username"]]
                        passwords += [results["Password"]]


                    # while loop that will continue until the correct username and password are entered
                    while not login:

                        check_username = input("Enter your username: ")

                    # if/else conditions to first check user input against database usernames stored in a list
                        if check_username not in usernames:
                            print("Username does not match!")
                            continue

                        elif check_username in usernames:
                            print("Username match!")
                            check_password = input("Enter your password: ")

                            # if/else condition to check password upon successful username match
                            # correct password ends the loop and allows the user to choose options from the submenu
                            if check_password not in passwords:
                                print("The password you entered is incorrect. Try again")
                                continue

                            elif check_password in passwords:
                                print("You have entered the correct password")
                                login = True

                except Exception as e:
                    print("User login error!")
                    raise e

            # call the check function
            check()

            # logged-in user can now access the submenu
            sub_menu()
            option = str(input("Please enter your option using the correct numeric key: "))

            # option 3 lets the user check their current wallet
            if option == "3":
                print("\nThis section will eventually have more functionality to let the user view wallet information")

            # option 4 can be used to search the crypto_prices collection to find relevant information for the user
            if option == "4":
                print("\nYou have selected the option to find information about the current crypto market")

                try:

                    crypto_id = []
                    crypto_current_price = []
                    crypto_market_cap = []
                    crypto_high_24h = []
                    crypto_low_24h = []

                    # iterate through the crypto_prices collections imported from the API
                    # store the values in the previously created empty lists
                    for query in db.crypto_prices.find().limit(10):
                        crypto_id += [query["id"]]
                        crypto_current_price += [query["current_price"]]
                        crypto_market_cap += [query["market_cap"]]
                        crypto_high_24h += [query["high_24h"]]
                        crypto_low_24h += [query["low_24h"]]

                    # save the pandas
                    crypto_panda = pandas.DataFrame({"ID": crypto_id,
                                                     "Current Price": crypto_current_price,
                                                     "Market Cap": crypto_market_cap,
                                                     "24 Hour High": crypto_high_24h,
                                                     "24 Hour Low": crypto_low_24h
                                                     })

                    # print the data frame...look at that Desiigner output (panda, panda, panda)
                    print(crypto_panda)

                except Exception as e:
                    print("Error finding the inputted information!")
                    raise e

            # option 5 lets the user make updates to their user profile
            if option == "5":
                print("\nYou have selected to update your user profile")

                # update function is defined to let the user make updates to his or her profile
                def update():

                    try:
                        update_profile = input("Enter your password again if you wish to make changes: ")
                        update_username = input("Choose a new username: ")
                        update_password = input("Choose a new password: ")

                        db.Users.update_one(
                            {"Password": update_profile},
                            {
                                "$set": {
                                    "Username": update_username,
                                    "Password": update_password
                                }
                            }
                        )
                        print("Record updated successfully!")

                    except Exception as e:
                        print("Record did not update!")
                        raise e

                # call the update function
                update()

            # option 6 lets the logged-in user delete their profile
            elif option == "6":
                print("\nYou have selected to delete your user profile!")

                # define a delete function which will permit a logged-in user to delete his or her profile
                def delete():
                    try:
                        delete_profile = input("Enter your password again if you are entirely sure:")
                        db.Users.delete_many({"Password": delete_profile})
                        print("User profile has been deleted!")

                    except Exception as e:
                        print("Profile failed to delete properly!")
                        raise e

                # call the delete function
                delete()

            # option 0 in the submenu allows the user to return to the main menu
            elif option == "0":
                print("\nyou have chosen to return to the main menu")

            # the else statement alerts the user to an invalid menu option
            else:
                print("\nInvalid option please use the correct numeric key")

        # option 0 in the main menu will exit the program
        elif option == "0":
            print("\nyou have chosen to exit the program")

        # else statement alerts the user to an invalid menu option
        else:
            print("\nInvalid option please use the correct numeric key")

        # call the menu function
        menu()
        option = str(input("Please enter your option using the correct numeric key: "))

        # customer appreciation
        print("Thanks for using this program. Hope to see you again!")






