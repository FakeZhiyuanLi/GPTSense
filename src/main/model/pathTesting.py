import os

currDir = os.path.abspath(__file__)
parentDir = os.path.abspath(os.path.join(currDir, '..'))
testDir = os.path.abspath(os.path.join(currDir, '..', '..'))
print(currDir)
print(parentDir)
print(testDir)