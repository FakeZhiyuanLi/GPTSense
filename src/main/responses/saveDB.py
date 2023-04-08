from connectDB import connectToMongoDBResponses

responses = connectToMongoDBResponses()
factoidResponses = responses['FactoidWebquestionsGPT']

def getGPTReponseFileSizes():
    trainSize = factoidResponses.count_documents({"file":"tgt-train"})
    devSize = factoidResponses.count_documents({"file":"tgt-dev"})
    testSize = factoidResponses.count_documents({"file":"tgt-test"})

    return {"tgt-train":trainSize, "tgt-dev":devSize, "tgt-test":testSize}

def saveGPTResponses(verbosity):
    '''
    tgt-train
    tgt-dev
    tgt-test
    '''

    sizes = getGPTReponseFileSizes()  
    fileNames = ["tgt-train", "tgt-dev", "tgt-test"]
    documentsAdded = 0

    for fileName in fileNames:
        file = open("/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/Responses/FactoidResponsesGPT/" + fileName + ".txt", "w")
        documents = factoidResponses.find({"file": fileName})
        for i in range(sizes[fileName]):
            document = documents.next()
            length = len(document['Answer'])
            if length > 200:
                file.write(document['Answer'] + ";\n")
                documentsAdded += 1
                if verbosity:
                    print("Added document length: " + str(length))
            else:
                if verbosity:
                    print("Rejected document length: " + str(length))
    if verbosity:
        print(documentsAdded)


if __name__ == '__main__':
    writeConfirmation = input("Confirm write? (y/n): ")
    if writeConfirmation.lower() == "y":
        saveGPTResponses(verbosity=False)