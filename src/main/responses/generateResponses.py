from utils.cert import pathToKey
from connectDB import connectToMongoDBQuestions, connectToMongoDBResponses
from openai.error import RateLimitError
import openai
import retry
import time

OpenAIKEYFile = open(pathToKey)
openai.api_key = OpenAIKEYFile.read()

QuestionDataset = connectToMongoDBQuestions()['FactoidWebquestions']
ResponseDataset = connectToMongoDBResponses()['FactoidWebquestionsGPT']

designation = int(input("Enter the designation (1-71): "))
lastQuestion = int(input("Enter the last question that was answered #: "))

documents = (QuestionDataset.find({"Designation":designation}))
size = QuestionDataset.count_documents({"Designation":designation})

# this is probably really dumb
for i in range(lastQuestion):
    documents.next()

@retry.retry(exceptions=RateLimitError, delay=2, backoff=3, max_delay=30, tries=15)
def getGPTAnswer(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":question['Question']}],
        temperature=1,
        max_tokens=1500
    )
    return response

for i in range(size):
    question = documents.next()
    lastQuestion += 1

    startTime = time.time()
    response = getGPTAnswer(question)
    endTime = time.time()
    diff = endTime - startTime

    print("Question #" + str(lastQuestion))
    print("Time spent: " + str(diff))
    print("Q: " + question['Question'])

    if "As an AI" in response['choices'][0]['message']['content'] or "sorry" in response['choices'][0]['message']['content'] or "Sorry" in response['choices'][0]['message']['content']:
        print("A: N/A")
    else:
        print("A: " + (response['choices'][0]['message']['content']))
        ResponseDataset.insert_one({"Question":question['Question'], "Answer":response['choices'][0]['message']['content'], "file":question['file'], "Designation":question['Designation']})