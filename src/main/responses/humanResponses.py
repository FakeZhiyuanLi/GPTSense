import xmltodict
import os

base = "/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/HumanResponses/Blogs/"
files = os.listdir("/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/HumanResponses/Blogs")
blogsFile = open("/Users/zhiyuan/Desktop/Hackathon/GPTSense/datasets/Responses/Human/blogs/blogs.txt", 'w')
succesful = 0


for i in range(len(files)):
    path = files[i]

    try:
        with open(base + path) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
        posts = data_dict['Blog']['post']
        for post in posts:
            if "urlLink" in post or "https" in post or "www." in post:
                continue
            if (len(post) > 100 and len(post) < 1000):
                
                blogsFile.write(post + "\n")
                succesful += 1
            else:
                break

    except:
        pass

print("num succesful: " + str(succesful))