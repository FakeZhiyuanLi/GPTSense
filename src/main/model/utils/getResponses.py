import re
import os

datasetsPath = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "..", "datasets"))

def getBlogResponses(fileName):
    file = open(os.path.abspath(os.path.join(datasetsPath, "Responses", "Human", "blogs", fileName + ".txt")))
    
    responses = []

    lines = file.readlines()
    for line in lines:
        if len(line) > 100 and len(line) < 1000:
            response = line.lower().strip()
            
            # this is very dumb but I am far too lazy to fix it
            response = re.sub(' +', ' ', response)
            response = re.sub('\\.\\.', '', response)
            response = re.sub('\\!\\!', '', response)
            response = re.sub('\\,\\,', '', response)
            response = re.sub('\\-\\-', '', response)
            response = re.sub('\\?\\?', '', response)

            responses.append(response)

    return responses

def getBlogResponseLength(fileName):
    file = open(os.path.abspath(os.path.join(datasetsPath, "Responses", "Human", "blogs", fileName + ".txt")))
    return len(file.readlines())

def getGPTResponses(fileName):
    file = open(os.path.abspath(os.path.join(datasetsPath, "Responses", "FactoidResponsesGPT", fileName + ".txt")))
    return file.readlines()

if __name__ == '__main__':
    # print(getBlogResponses("blogs"))
    pass