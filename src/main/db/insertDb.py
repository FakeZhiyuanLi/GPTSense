from connectDB import connectToMongoDB
from utils.fileNames import tgt_train, tgt_dev, tgt_test
import sys

db = connectToMongoDB()
questionDB = db['FactoidWebquestions']

def getDataset(directory):
    directory = directory.lower()

    if directory == "insert":
        key, val = input("(key, val): ").strip().split()
        questionDB.insert_one({key:val})
        sys.exit()
    elif directory == "train":
        dataset = open(tgt_train, "r")
    elif directory == "test":
        dataset = open(tgt_test, "r")
    elif directory == "dev":
        dataset = open(tgt_dev, "r")
    else:
        try:
            dataset = open(directory, "r")
        except:
            print("file not found")
            sys.exit()

    return dataset

def readDatasetToList(dataset):
    questions = []

    while True:
        try:
            question = dataset.readline().strip()
            if question == '':
                break
            question = question.replace("?", "")
            questions.append(question)
        except:
            break

    return questions

if __name__ == '__main__':
    directory = input("Enter full directory of .txt file ('insert' to test an insert) \nOR 'train' for tgt-train, 'test' for tgt-test, 'dev' for tgt-dev: ")
    fileName = input("Enter file name to set in MongoDB, ex. ('tgt-dev'): ")

    dataset = getDataset(directory)
    questions = readDatasetToList(dataset)
    questionsJSON = []
    datasetSize = len(questions)

    curr = 0
    designation = 0

    for question in questions:
        if curr % 1000 == 0:
            designation += 1
        curr += 1
        questionsJSON.append({"Question":question, "file": fileName, "Designation":designation})

    questionDB.insert_many(questionsJSON)
