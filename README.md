Project0_crypto_wallet

Project Description

The overall goal of this project was to develop an application in Python that would utilize basic Create, Read, Update, and Delete operations. My decision to develop an application that would act as a cryptocurrency wallet was overly ambitious at this point in my developer career; however, I was able to create a basic login system where a user can then access information 
pertaining to the current crypto market in addition to updating or deleting their current profile. The application connects to a well-known API where data from the current crypto market is saved in a JSON file and then stored in its own collection in MongoDB. Everything was done locally with a PyMongo driver establishing a connection to MongoDB which could handle data collection and queries in real-time. This project was developed in IntelliJ. 
Technologies Used:

•	Python 3.10
•	MongoDB

•	PyMongo

•	MongoDBCompass

Features:

•	A menu system that a user can access to either create a new user profile or login to an existing one.

•	Functions to create a new user profile, read existing documents stored in two collections, update a user profile, and/or delete a current user profile.

•	A login system to check username and password against queried documents within the Users collection.

•	A sub menu accessible after a successful user login with further options to check current cryptocurrency prices outputted in a DataFrame using Pandas, update a user profile, or delete a user profile.

•	A __name__ == ‘__main__’ to run the entire script.

To-do list:

•	A better user login system with more security when validating credentials.

•	More efficient code.

•	Greater user functionality with an option to store more user data.

•	Test cases and better usage of unit testing.

Creator:

•	Michael Celusniak 

