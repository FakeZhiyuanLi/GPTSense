from connectDB import connectToMongoDBResponses

responses = connectToMongoDBResponses()
factoidResponses = responses['FactoidWebquestionsGPT']

if __name__ == '__main__':
    confirmation = input("Confirm clear? (y/n): ")
    if confirmation.lower() == "y":
        factoidResponses.delete_many({"Answer":{"$regex":"as an AI"}})
        print(factoidResponses.count_documents({"Answer":{"$regex":"as an AI"}}))