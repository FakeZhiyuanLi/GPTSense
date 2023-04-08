from connectDB import connectToMongoDB

db = connectToMongoDB()
questions = db['FactoidWebquestions']

if __name__ == '__main__':
    confirmation = input("Confirm clear? (y/n): ")
    if confirmation.lower() == "y":
        questions.delete_many({})