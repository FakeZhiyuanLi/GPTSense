from pymongo import MongoClient
from utils.cert import pathToCert

def connectToMongoDBResponses():
    uri = "mongodb+srv://gptsensedb.u6c6rqd.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    client = MongoClient(uri, tls=True, tlsCertificateKeyFile=pathToCert)

    return client['Responses']
    
def connectToMongoDBQuestions():
    uri = "mongodb+srv://gptsensedb.u6c6rqd.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
    client = MongoClient(uri, tls=True, tlsCertificateKeyFile=pathToCert)

    return client['Questions']