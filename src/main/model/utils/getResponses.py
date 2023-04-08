import re

def getBlogResponses(fileName):
    file = open("/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/Responses/Human/blogs/" + fileName + ".txt")
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
    file = open("/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/Responses/Human/blogs/" + fileName + ".txt")
    return len(file.readlines())

def getGPTResponses(fileName):
    file = open("/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/Responses/FactoidResponsesGPT/" + fileName + ".txt")
    return file.readlines()

if __name__ == '__main__':
    pass