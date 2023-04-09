import os

NGQFolder = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', '..', 'datasets', 'NGQ'))
certificationFolder = os.path.abspath(os.path.join(__file__, '..', '..', '..', '..', '..', 'CertificationFiles'))

tgt_train = os.path.abspath(os.path.join(NGQFolder, "tgt-train.txt"))
tgt_dev = os.path.abspath(os.path.join(NGQFolder, "tgt-dev.txt"))
tgt_test = os.path.abspath(os.path.join(NGQFolder, "tgt-test.txt"))

pathToCert = os.path.abspath(os.path.join(certificationFolder, "mongoDBKey.pem"))

# tgt_train = "/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/NGQ/tgt-train.txt"
# tgt_dev = "/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/NGQ/tgt-dev.txt"
# tgt_test = "/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/NGQ/tgt-test.txt"
# pathToCert = "/Users/zhiyuan/Desktop/Hackathon/GPTSense/CertificationFiles/mongoDBKey.pem"