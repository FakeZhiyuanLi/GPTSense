from connectDB import connectToMongoDBResponses

responses = connectToMongoDBResponses()
factoidResponses = responses['FactoidWebquestionsGPT']

if __name__ == '__main__':
    confirmation = input("Confirm clear? (y/n): ")
    if confirmation.lower() == "y":
        factoidResponses.delete_many({"Designation":33})
        print(factoidResponses.count_documents({"Designation":33}))