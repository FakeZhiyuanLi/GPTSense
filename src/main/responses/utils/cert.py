import os

certificationFilesPath = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "..", "CertificationFiles"))

pathToCert = os.path.join(certificationFilesPath, "mongoDBKey.pem")
pathToKey = os.path.join(certificationFilesPath, "OpenAIKey.txt")