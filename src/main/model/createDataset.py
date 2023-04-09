import os
from utils.getResponses import getBlogResponses, getGPTResponses, getBlogResponseLength

GPTSensePath = os.path.abspath(os.path.join(__file__, "..", "..", "..", ".."))
# tfDatasetBase = "/Users/zhiyuan/Desktop/Hackathon/GPTSense/tfDatasets/"
tfDatasetBase = os.path.join(GPTSensePath, "tfDatasets")

def createHumanResponses(): 
    # 70 20 10 split train, test, val
    # only files is blogs.txt
    fileSize = getBlogResponseLength("blogs")
    splits = {"train":int(fileSize*0.7),"test":int(fileSize*0.2),"validation":int(fileSize*0.1)}
    humanResponses = getBlogResponses("blogs")
    idx = 0
    seen = set()

    for split in splits.keys():
        fileIdx = 0
        for i in range(splits[split]):
            if idx >= len(humanResponses):
                break
            response = humanResponses[idx]
            idx += 1
            if response in seen:
                continue
            seen.add(response)

            file = open(tfDatasetBase + "/" + split + "/HumanResponses/" + str(fileIdx) + ".txt", 'w')
            file.write(response)

            fileIdx += 1

def createGPTResponses():
    fileNames = ["tgt-train", "tgt-test", "tgt-dev"]

    for fileName in fileNames:
        idx = 0
        GPTResponses = getGPTResponses(fileName)
        fileSize = len(GPTResponses)
        splits = {"train":int(fileSize*0.7),"test":int(fileSize*0.2),"validation":int(fileSize*0.1)}

        for split in splits.keys():
            fileIdx = 0
            response = ""
            for i in range(splits[split]):
                if idx >= len(GPTResponses):
                    break

                response += (GPTResponses[idx].strip())
                if ";" in response:
                    response = response.replace(';','')
                    
                    if len(response) < 5:
                        continue

                    file = open(tfDatasetBase + "/" + split + "/GPTResponses/" + str(fileIdx) + ".txt", 'w')
                    file.write(response.strip())
                    response = ""
                    fileIdx += 1

                idx += 1

if __name__ == "__main__":
    createHumanResponses()
    createGPTResponses()
    pass