import os

NGQFolder = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "..", "datasets", "NGQ"))
certificationFolder = os.path.abspath(os.path.join(__file__, "..", "..", "..", "..", "..", "CertificationFiles"))

tgt_train = os.path.abspath(os.path.join(NGQFolder, "tgt-train.txt"))
tgt_dev = os.path.abspath(os.path.join(NGQFolder, "tgt-dev.txt"))
tgt_test = os.path.abspath(os.path.join(NGQFolder, "tgt-test.txt"))

pathToCert = os.path.abspath(os.path.join(certificationFolder, "mongoDBKey.pem"))